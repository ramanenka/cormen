def matrix_multiply(a, b):
    cols = len(a[0]) if len(a) > 0 else 0
    rows = len(b)

    if cols != rows:
        raise AssertionError('Matrices are not compatible')

    ccols = len(b[0]) if len(b) > 0 else 0
    crows = len(a)

    c = [[0 for x in range(ccols)] for x in range(crows)]

    for i in range(crows):
        for j in range(ccols):
            for k in range(cols):
                c[i][j] = c[i][j] + a[i][k] * b[k][j]

    return c


def matrix_multiply_recursive(a, b):
    icols = len(a[0]) if len(a) > 0 else 0
    irows = len(b)

    if icols != irows:
        raise AssertionError('Matrices are not compatible')

    rows = len(a)
    cols = len(b[0]) if len(b) > 0 else 0

    c = [[0 for x in range(cols)] for x in range(rows)]

    _matrix_multiply_recursive(
            a, 0, len(a) - 1, 0, len(a[0]) - 1 if len(a) > 0 else 0,
            b, 0, len(b) - 1, 0, len(b[0]) - 1 if len(b) > 0 else 0,
            c, 0, len(c) - 1, 0, len(c[0]) - 1 if len(c) > 0 else 0)

    return c


def _matrix_multiply_recursive(a, arf, arl, acf, acl, b, brf, brl, bcf, bcl, c, crf, crl, ccf, ccl):
    if arf == arl:
        c[crf][ccf] += a[arf][acf] * b[brf][bcf]
        print('c[', crf, '][', ccf, '] += a[', arf, '][', acf, '] * b[', brf, '][', bcf, ']')
    else:
        arm = (arf + arl) // 2
        acm = (acf + acl) // 2
        brm = (brf + brl) // 2
        bcm = (bcf + bcl) // 2
        crm = (crf + crl) // 2
        ccm = (ccf + ccl) // 2

        #      cf  cm  cl
        # rf
        #        11  12
        # rm
        #        21  22
        # rl

        # C11 = A11 * B11 + A12 * B21
        _matrix_multiply_recursive(a, arf, arm, acf, acm,
                                   b, brf, brm, bcf, bcm,
                                   c, crf, crm, ccf, ccm)

        _matrix_multiply_recursive(a, arf, arm, acm + 1, acl,
                                   b, brm + 1, brl, bcf, bcm,
                                   c, crf, crm, ccf, ccm)

        # C12 = A11 * B12 + A12 * B22
        _matrix_multiply_recursive(a, arf, arm, acf, acm,
                                   b, brf, brm, bcm + 1, bcl,
                                   c, crf, crm, ccm + 1, ccl)

        _matrix_multiply_recursive(a, arf, arm, acm + 1, acl,
                                   b, brm + 1, brl, bcm+1, bcl,
                                   c, crf, crm, ccm + 1, ccl)

        # C21 = A21 * B11 + A22 * B21
        _matrix_multiply_recursive(a, arm + 1, arl, acf, acm,
                                   b, brf, brm, bcf, bcm,
                                   c, crm + 1, crl, ccf, ccm)

        _matrix_multiply_recursive(a, arm + 1, arl, acm + 1, acl,
                                   b, brm + 1, brl, bcf, bcm,
                                   c, crm + 1, crl, ccf, ccm)

        # C22 = A21 * B12 + A22 * B22
        _matrix_multiply_recursive(a, arm + 1, arl, acf, acm,
                                   b, brf, brm, bcm + 1, bcl,
                                   c, crm + 1, crl, ccm + 1, ccl)

        _matrix_multiply_recursive(a, arm + 1, arl, acm + 1, acl,
                                   b, brm + 1, brl, bcm + 1, bcl,
                                   c, crm + 1, crl, ccm + 1, ccl)
