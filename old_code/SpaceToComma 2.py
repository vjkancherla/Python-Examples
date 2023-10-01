with open('/Users/vija0326/Downloads/624148721429_elasticloadbalancing_eu-west-1_NandosSAMW-ELB_20180429T1115Z_52.18.229.77_4zg66muo.log', 'r+') as f:
    text = f.read()
    f.seek(0)
    f.truncate()
    f.write(text.replace(' ', ','))