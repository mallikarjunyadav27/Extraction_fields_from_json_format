import json
import re

# f = open(r'C:\Users\Lenovo\OneDrive\Desktop\TREES\json_output_files\json_file3.json')
# data = json.load(f)
# print(data)
# empt_dict = {}

def regex_certificate_no(val):
    up_val = []
    try:
        if type(val) == str:
            return val
        else:
            for i in val:
                i = i.replace(" ", "")
                result = re.search(r"^MPN-[0-9]{6}$", i)
                result1 = re.search(r"^[0-9]{7}$", i)
                r1 = re.findall(r"[0-9]{6}", i)
                if result is None and result1 is not None:
                    res = re.findall(r"[0-9]{7}", i)
                    if res is not None:
                        if res[0][1:] not in up_val:
                            return res[0][1:]
                if result is not None:
                    if r1 is not None:
                        if r1[0] not in up_val:
                            return r1[0]


    except Exception as e:
        print(e)
    return up_val
def rgex_shipping_marks(val):
    up_val = []
    try:
        for i in val:
            if re.search(r'^[0-9]{1,10}$', i) is None:
                val.remove(i)
            elif i not in up_val:
                up_val.append(i)
    except Exception as e:
        print(e)
    return up_val
def rgex_shipper_ref(val):
    up_val = []
    try:
        for i in val:
             result = re.search(r"^SHIPPER'S NO. [0-9]{1,11}-[0-9]{1}$", i)
             result1 = re.search(r"^[A-Z0-9]{1,11}$",i)
             result2 = re.search(r"^Shipper Ref #: [0-9]{1,6}$", i)
             result3 = re.search(r"^[0-9]{1,9}-[0-9]{1}$", i)
             result4 = re.search(r"^SHIPPER'S NO. [0-9]{1,11}$", i)
             r1 = re.findall(r"[0-9]{1,11}", i)
        if result is None and result1 is not None:
             r2 = re.findall(r"[A-Z0-9]{1,11}",i)

             if r2[2] is not None:
                 if r2[2] not in up_val:
                     return r2[2]

        if result is not None:
            if r1 is not None:
                if r1 not in up_val:
                    return r1[0]
        if result2 is not None:
            r3 = re.findall(r"[0-9]{1,6}", i)
            if r3[0:] is not None:
                if r3[0:] not in up_val:
                    return r3[0:]
        if result2 is not None:
            r3 = re.findall(r"[0-9]{1,6}", i)
            if r3[0:] is not None:
                if r3[0:] not in up_val:
                    return r3[0:]
        if result3 is not None:
            r4 = re.findall(r"[0-9]{1,11}", i)
            if r4[0] is not None:
                if r4[0] not in up_val:
                    return r4[0]
        if result4 is not None:
            r5 = re.findall(r"[0-9]{1,11}", i)

            if r5[0] is not None:
                if r5[0] not in up_val:
                    return r5[0]
    except Exception as e:
        print(e)
    return up_val
def regex_bolNo(val):
    up_val = []
    try:
        for i in val:
            result = re.search(r"^BOL #: [A-Za-z]{2}-[0-9]{6}", i)
            result1 = re.search(r"^BOL #: [0-9]{4}-[0-9]{7}", i)
            r1 = re.findall(r"[A-Za-z]{2}-[0-9]{6}", i)
            if result is None and result1 is not None:
                r2 = re.findall(r"[0-9]{4}-[0-9]{7}", i)
                if r2 is not None:
                    if r2 not in up_val:
                        return r2
            if result is not None:
                if r1 is not None:
                    if r1 not in up_val:
                        return r1[0]

    except Exception as e:
        print(e)
    return up_val

def rgex_po_num(val):
    up_val = []
    try:
        for i in val:
            result = re.search(r"^PO #: [0-9]{4}/[A-Z]{3}/[0-9]{2}$", i)
            result1 = re.search(r"^PO #: [0-9]{1,6}$",i)
            r1 = re.findall(r'[0-9]{4}/[A-Z]{3}/[0-9]{2}', i)
            if result is None and result1 is not None:
                r2 = re.findall(r"[0-9]{1,6}", i)
                if r2 is not None:
                    if r2 not in up_val:
                        return r2
            if result is not None:
                if r1 is not None:
                    if r1 not in up_val:
                        return r1[0]
            return result
    except Exception as e:
        print(e)

    return up_val
def rgex_order_num(val):
    up_val = []
    try:
        for i in val:
            result = re.search(r"^[0-9]{1,6}$", i)

            if result is not None:
                r1 = re.findall(r"[0-9]{1,6}", i)
                if r1[0:] is not None:
                    if r1[0:] not in up_val:
                        return r1[0:]

    except Exception as e:
        print(e)
    return up_val
def extract(data):
    for i in data:
        if i == "certificateNo":
            data[i] = regex_certificate_no(data[i])
        if i == "shippingMarks":
            data[i] = rgex_shipping_marks(data[i])
        if i == "shipperRef":
            data[i] = rgex_shipper_ref(data[i])


        if i == "bolNo":
            data[i] = regex_bolNo(data[i])
        if i == "bolNo":
            if len(data[i]) == 0:
                data[i] = data["shipperRef"]
            else:
                data[i] = data[i]
        if i == "poNo":
            data[i] = rgex_po_num(data[i])
        if i == "orderNo":
            data[i] = rgex_order_num(data[i])
    final = (data.pop("shipperRef"))
    return data
