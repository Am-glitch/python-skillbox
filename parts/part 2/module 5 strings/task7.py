def validate_ip(ip):
    octets = [octet for octet in ip.split('.')]

    if len(octets) < 4:
        return  'Адрес — это четыре числа, разделённые точками'
        
    for octet in octets:
        if not octet.isdigit():
            return f'{octet} - это не целое число'
        if int(octet) > 255:
            return f'{octet} превышает 255'
            
    return 'IP-адрес корректен'

ip = input('Введите IP: ')

print(validate_ip(ip))