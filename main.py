data = {}
arr = []


def get_rs_via_ow():
    import xml.dom.minidom as et

    a = et.parse("RS_ViaOW.xml")
    b = a.documentElement
    data = {}
    flights = b.getElementsByTagName("Flights")
    for flight in flights:
        c = flight.getElementsByTagName("Flights")
        for m in c:
            d = m.getElementsByTagName("Flight")
            for j in d:
                flight_umber = j.getElementsByTagName('FlightNumber')[0].childNodes[0].nodeValue  # Parvoz raqami
                departure_time_stamp = j.getElementsByTagName('DepartureTimeStamp')[0].childNodes[
                    0
                ].nodeValue  # Uchish vaqti
                arrival_time_stamp = j.getElementsByTagName('ArrivalTimeStamp')[0].childNodes[
                    0].nodeValue  # qo'nish vati
                data['flight_number'] = flight_umber
                data['departure_time_stamp'] = departure_time_stamp
                data['arrival_time_stamp'] = arrival_time_stamp
                arr.append(data)
    return arr


def get_rs_via_3():
    import xml.etree.ElementTree as et
    tree = et.parse("RS_Via-3.xml")
    root = tree.getroot()
    for priced in root[1]:
        for onward in priced[0]:
            for date in onward:
                data["flight_number"] = date[1].text
                data["departure_time_stamp"] = date[4].text
                data["arrival_time_stamp"] = date[5].text
                arr.append(data)
    return arr


# get_rs_via_3()
print(get_rs_via_ow())
