def FDollar2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.2f}".format(DollarValue)

    return DollarValueStr


def FDollar0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "${:,.0f}".format(DollarValue)

    return DollarValueStr


def FComma2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "{:,.2f}".format(DollarValue)

    return DollarValueStr


def FComma0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "{:,.0f}".format(DollarValue)

    return DollarValueStr


def FNumber0(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "{:.0f}".format(DollarValue)

    return DollarValueStr


def FNumber2(DollarValue):
    # Function will accept a value and format it to $#,###.##.

    DollarValueStr = "{:.2f}".format(DollarValue)

    return DollarValueStr