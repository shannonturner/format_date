def format_date(date, desired_format='%Y-%m-%d'):

    """ Attempts to standardize a given date into the desired_format.
        Returns the date in the desired format on success or False on failure.
        See http://docs.python.org/2/library/datetime.html#strftime-and-strptime-behavior for formatting details.
    """

    from datetime import datetime

    formats_to_try = ('%m/%d/%Y', '%m/%d/%y', '%m-%d-%Y', '%m-%d-%y', '%m.%d.%Y', '%m.%d.%y',
                      '%m/%d', '%m-%d', '%m.%d', '%B %d, %Y', '%b %d, %Y', '%d-%b-%y', '%d-%b-%Y',
                      '%d/%b/%y', '%d/%b/%Y', '%d.%b.%y', '%d.%b.%Y',
                      )

    for dateformat in formats_to_try:
        try:
            date = datetime.strptime(date, dateformat).strftime(desired_format)
            break
        except ValueError:
            pass
    else:
        return False

    return date

##dates_to_try = (
##    '3/14/2012',
##    'March 14, 2012',
##    '03/14/12',
##    '03.14.2012',
##    '14-Mar-2012',
##    '14-Mar-12',
##    )
##
##for date_ in dates_to_try:
##    print date_, '\t\t', format_date(date_)
