
#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "bootsel-reboot.hpp"
#include "unistd.h"
#include "pico/time.h"

int main() {
    stdio_init_all();

    const uint LED_PIN_SLAVE = 13;
    gpio_init(LED_PIN_SLAVE);
    gpio_set_dir(LED_PIN_SLAVE, GPIO_OUT);

    const uint SDIO_CMD_PIN = 5;  // cmd - pin
    const uint SDIO_DATA_PIN = 6; // data - pin

    gpio_init(SDIO_CMD_PIN);
    gpio_set_dir(SDIO_CMD_PIN, GPIO_IN); // Set command pin - as input

    gpio_init(SDIO_DATA_PIN);
    gpio_set_dir(SDIO_DATA_PIN, GPIO_IN); // Set data pin - as input
 
    while (true) {
        // Check if a command is received (command pin - high)
        if (gpio_get(SDIO_CMD_PIN)) {
            char received_char = 0;

            // Receive one character at a time
            for (int i = 0; i < 8; i++) {
                received_char |= (gpio_get(SDIO_DATA_PIN) << i);

                // Delay briefly between reading each bit
                sleep_ms(100); 
            }
            
            // Process the received character (e.g., print it)
            printf("Received: %x\n", received_char);

           // printf("Received: %c\n", received_char);

            // Toggle an LED to indicate data reception
            gpio_put(LED_PIN_SLAVE, 1);
            sleep_ms(1000);
            gpio_put(LED_PIN_SLAVE, 0);
        }
    }

    return 0;
}
