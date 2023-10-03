#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "bootsel-reboot.hpp"
#include "unistd.h"
#include "pico/time.h"

int main() {
    stdio_init_all();

    const uint LED_PIN = 13;
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    const uint SDIO_CMD_PIN = 2;  // pin command
    const uint SDIO_DATA_PIN = 3; // pin data

    gpio_init(SDIO_CMD_PIN);
    gpio_set_dir(SDIO_CMD_PIN, GPIO_OUT);
    gpio_put(SDIO_CMD_PIN, 0); // Command pin - low initially

    gpio_init(SDIO_DATA_PIN);
    gpio_set_dir(SDIO_DATA_PIN, GPIO_OUT);
    sleep_ms(2000);

    while (true) {
        // Host sends a message
        const char* message = "hello";
        for (int i = 0; message[i]; i++) {
            
            gpio_put(SDIO_CMD_PIN, 1); // Command pin - high for character transmission start
                
            char c = message[i];
            for(int j=0; j<8; j++){
                gpio_put(SDIO_DATA_PIN, c&0x80); // Send one character at a time
                c<<=1;
                sleep_ms(100); 

            }
            gpio_put(SDIO_CMD_PIN, 0); // Command pin - low for character transmission end
            
            // Toggle an LED to indicate character transmission
            gpio_put(LED_PIN, 1);
            sleep_ms(1000);
            gpio_put(LED_PIN, 0);
        }
        sleep_ms(2000); // Delay between messages
    }

    return 0;
}

