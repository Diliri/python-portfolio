passwordFile = open('SecretPasswordFile.txt')

secretPassword = passwordFile.read()
print('Введіть пароль. ')
typedPasswd = input()
if typedPasswd == secretPassword:       # тобто у файлі всього-то ОДИН пароль
    print('Доступ дозволено. ')
    if typedPasswd == '12345':
            print('Рекомендуємо встановити більш складний пароль! ')
else:
    print('У доступі відмовлено. ')