
#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "unistd.h"

int main() {
    stdio_init_all();

    const uint SDIO_CMD_PIN = 5;  // pin command
    const uint SDIO_DATA_PIN = 6; // pin data
    const uint LED_PIN = 13;      // pin for LED (LED 2 ON Bread board)

    gpio_init(SDIO_CMD_PIN);
    gpio_set_dir(SDIO_CMD_PIN, GPIO_IN);

    gpio_init(SDIO_DATA_PIN);
    gpio_set_dir(SDIO_DATA_PIN, GPIO_IN);

    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    while (true) {
        // Wait for the start of character transmission (command PIN high)
        while (!gpio_get(SDIO_CMD_PIN)) {
            sleep_us(10); 
        }

        // Receive 4 bits of data at a time
        char receivedData = 0;
        for (int i = 0; i < 4; i++) {
            receivedData |= (gpio_get(SDIO_DATA_PIN) << i);
            // Wait for the next data bit
            sleep_us(10);
        }


        char originalChar = receivedData + '0'; 


        printf("Received Character: %x\n", originalChar);

        // Blink the LED to indicate character reception
        gpio_put(LED_PIN, 1);
        sleep_ms(500); // LED on for 500 ms
        gpio_put(LED_PIN, 0);

        // Wait for the end of character transmission (command pin - low)
        while (gpio_get(SDIO_CMD_PIN)) {
            sleep_us(10); //
        }

        // Small delay before listening for the next character
        sleep_ms(100);
    }

    return 0;
}
