from gpiozero import LED
import time

dot = float(input('Въведете продължителността на един интервал(напр. 0.3):   '))
message = (input("Въведете съобщението с разделител '_' между думите(напр: Welcome_Ivan):  ")).lower()
print(message)

led = LED(2, initial_value=False)
dash = dot * 3
end_of_word = dot * 7
end_of_letter = dot * 3
letter =[]
morse_dict = {
    'a': [dot, dash], 'b': [dash, dot, dot, dot], 'c': [dash, dot, dash, dot], 'd': [dash, dot, dot], 'e': [dot],
    'f': [dot, dot, dash], 'g': [dash, dash, dot], 'h': [dot, dot, dot, dot], 'i': [dot, dot],
    'j': [dot, dash, dash, dash],
    'k': [dash, dot, dash], 'l': [dot, dash, dot, dot], 'm': [dash, dash], 'n': [dash, dot], 'o': [dash, dash, dash],
    'p': [dot, dash, dash, dot], 'q': [dash, dash, dot, dash], 'r': [dot, dash, dot], 's': [dot, dot, dot], 't': [dash],
    'u': [dot, dot, dash], 'v': [dot, dot, dot, dash], 'w': [dot, dash, dash], 'x': [dash, dot, dot, dash],
    'y': [dash, dot, dash, dash], 'z': [dash, dash, dot, dot], '1': [dot, dash, dash, dash, dash],
    '2': [dot, dot, dash, dash, dash], '3': [dot, dot, dot, dash, dash], '4': [dot, dot, dot, dot, dash],
    '5': [dot, dot, dot, dot, dot], '6': [dash, dot, dot, dot, dot], '7': [dash, dash, dot, dot, dot],
    '8': [dash, dash, dash, dot, dot], '9': [dash, dash, dash, dash, dot], '10': [dash, dash, dash, dash, dash],
    '_': end_of_word
}
for char in message:
    if char in morse_dict:
        if char == '_':
            led.off()
            time.sleep(end_of_word)
            continue
        else:
            letter.append(morse_dict.get(char))
            for seconds in letter:
                led.on()
                time.sleep(seconds)
                led.off()
                time.sleep(dot)
    else:
        continue
    letter.clear()







