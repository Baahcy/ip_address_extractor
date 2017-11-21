import csv
import re


try:
    with open('JAR-16-20296A.txt') as csvfile:
        urlPattern = re.compile(r"""(\d{1,3})(\[\.\]) # First part of IP addr 127[.]
                          (\d{1,3})(\[\.\]) # Second part of IP 0[.]
                          (\d{1,3})(\[\.\])(\d{1,3}) # Third part""", re.X)
        countryPattern = r"This IP address is located in (\w.)*(\s\w+)*"

        reader = csv.DictReader(csvfile)
        for row in reader:
            ip_match_obj = re.match(urlPattern, row['INDICATOR_VALUE'])
            country_match_obj = re.search(countryPattern, row['DESCRIPTION'])
            try:
                if ip_match_obj and country_match_obj:
                    print(
                        re.sub(r"\[\.\]", ".", ip_match_obj.group()), '\t\t',
                        country_match_obj.group()
                        )
                elif ip_match_obj:
                    print(re.sub(r"\[\.\]", ".", ip_match_obj.group()))
            except AttributeError as err:
                print(err)

except IOError as IOerr:
    print(IOerr)
