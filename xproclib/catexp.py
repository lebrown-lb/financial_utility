#!/usr/bin/env python

import numpy as np
import re
import ntpath
from io import StringIO
import csv


mdx = ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC']


class ExpCat:
    def __init__(self, name, kwrds, trans, tcst, exps):
        self.name = name
        self.kwrds = kwrds
        self.trans = trans
        self.tcst = tcst
        self.exps = exps

    def add_kwrd(self, new_kwrd):
        self.kwrds = self.kwrds.rstrip()
        if len(self.kwrds) > 0:
            self.kwrds += ',' + new_kwrd
        else:
            self.kwrds += new_kwrd 
        print('[ADDED NEW KEY WORD]')


def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def srt_exps(fo):
    c = fo
    s = []
    while len(c) > 0:
        (a, b) = c[0][0], float(c[0][1])
        c = np.delete(c, (0), axis=0)

        idx = []
        for j in range(len(c)):
            if a == c[j][0]:
                b += float(c[j][1])
                b = np.around(b, decimals=2)
                idx.append(j)
        c = np.delete(c, idx, axis=0)
        s.append((len(idx) + 1, a, b))
    return np.array(s)


def findnth(haystack, needle, n):
    parts= haystack.split(needle, n+1)
    if len(parts)<=n+1:
        return -1
    return len(haystack)-len(parts[-1])-len(needle)


def prc_trans_csv(fp):
    with open(fp) as f:
        fs = f.read()
    f.close()

    f = StringIO(fs)
    rdr = csv.reader(f, delimiter=',')
    x = []
    for row in rdr:
        x.append(row)
    z = np.array(x)
    z = np.delete(z, (0), axis=0)
    return z


def prc_trans_srt(ts, desc_idx, vlu_idx):
    a = ts[:, desc_idx]
    b = ts[:, vlu_idx]

    idx = []
    for i in range(len(a)):
        if len(b[i]) <= 1:
            idx.append(i)

    a = np.delete(a, idx, axis=0)
    b = np.delete(b, idx, axis=0)

    fo = np.array([(a[i], b[i]) for i in range(len(a))])
    se = srt_exps(fo)
    return se


def prc_trans_merch_srch(ts, desc_idx, merch_desc):
    a = ts[:, desc_idx]
    e = []
    for i in range(len(a)):
        x = ts[i]
        if x[desc_idx] == merch_desc:
            e.append(x)
    return e


def prc_trans_msum(ts, date_idx, fi_idx, fo_idx):
    a = ts
    s = a[:, date_idx]

    # generate transactions grouped by month
    md = []
    while len(a):
        t = []
        if '/' in s[0]:
            (m, d, y) = s[0].split('/')
            e = m + '/(.*)/' + y
        elif '-' in s[0]:
            (y, m, d) = s[0].split('-')
            e = y + '-' + m + '-(.*)'
        t.append(a[0])
        a = np.delete(a, (0), axis=0)
        s = np.delete(s, (0), axis=0)

        idx = []
        for i in range(0, len(s)):
            if (re.match(e, s[i])):
                t.append(a[i])
                idx.append(i)

        a = np.delete(a, idx, axis=0)
        s = np.delete(s, idx, axis=0)

        md.append(np.array(t))


    # generate sums for each month
    # remove the '\n' term form strings and handle zero length strings
    ms = []
    for i in range(len(md)):
        y0 = [f.replace('\n', '') for f in md[i][:, fi_idx]]
        y1 = [f.replace('\n', '') for f in md[i][:, fo_idx]]
        fi = [(float(f) if len(f) else 0) for f in y0]
        fo = [(float(f) if len(f) else 0) for f in y1]
        ms.append((np.around([np.sum(fi), np.sum(fo)], decimals=2)).tolist())

    # calculate net cash flows for each month
    mn = np.around([ms[i][0]-ms[i][1] for i in range(len(ms))], decimals=2)
    mn = mn.tolist()

    mdat = []
    for i in range(len(md)):
        s = md[i][0][0]
        if '/' in s:
            (m, d, y) = s.split('/')
        elif '-' in s:
            (y, m, d) = s.split('-')
        mi = int(m) - 1

        m = mdx[mi]
        mdat.append(["{}-{}".format(m, y), str(ms[i][0]), str(ms[i][1]), str(mn[i])])

    mdat.append(["TOTAL", "", "", str(np.around(np.sum(mn), decimals=2))])

    return mdat


def prc_trans_exp_cat(uc_exps, xc_obj):
    tsm = 0
    tct = 0
    kwrds = xc_obj.kwrds.split(',')
    kwrds[-1].rstrip('\r\n')

    ce = []
    uce = uc_exps
    for p in kwrds:
        ce_idx = [i for i, k in enumerate(uce[:, 1]) if p in k]
        sm = 0
        ct = 0
        for i in ce_idx:
            ct += int(uce[i][0])
            sm += float(uce[i][2])
            ce.append(uce[i])
        uce = np.delete(uce, ce_idx, axis=0)
        tsm += sm
        tct += ct
    xc_obj.trans = tct
    xc_obj.tcst = tsm
    xc_obj.exps = ce
    return uce
