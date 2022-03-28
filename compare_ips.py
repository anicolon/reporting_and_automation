import pandas as pd
import ipaddress

ranges = pd.read_csv('/Users/anicolon/Desktop/compare_ips.csv')

operadora = ranges['Operadora'][ranges['Operadora'].notna()]
geoip = ranges['GeoIP'][ranges['GeoIP'].notna()]


def make_iprange_list(operadora):
    ranges = [range for range in operadora]
    ip_compare = dict.fromkeys(ranges)

    dicty_keys = ip_compare.keys()

    for i in dicty_keys:
        ip_compare[i] = [i for i in ipaddress.IPv4Network(str(i))]

    flat_list = []
    for sublist in list(ip_compare.values()):
        for item in sublist:
            flat_list.append(item)

    return flat_list


range_1 = make_iprange_list(operadora)
range_2 = make_iprange_list(geoip)

print(len(range_1))
print(len(range_2))

print(range_1 == range_2)
