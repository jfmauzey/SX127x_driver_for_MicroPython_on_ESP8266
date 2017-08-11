from time import sleep


def send(lora):

    counter = 0
    print("LoRa Sender")

    while True:
        # send packet
        lora.beginPacket()
        payload = 'Hello ({0})'.format(counter)
        print("Sending packet: ")
        print(payload, '\n')
        lora.print(payload)
        lora.endPacket()
        
        counter += 1
        sleep(5) 