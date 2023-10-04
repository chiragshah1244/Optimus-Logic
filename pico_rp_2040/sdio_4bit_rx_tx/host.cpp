
#include <stdio.h>
#include "pico/stdlib.h"
#include "hardware/gpio.h"
#include "unistd.h"

int main() {
    stdio_init_all();

    const uint LED_PIN = 13;
    gpio_init(LED_PIN);
    gpio_set_dir(LED_PIN, GPIO_OUT);

    const uint SDIO_CMD_PIN = 8;   // Command pin
    const uint SDIO_CLK_PIN = 7;   // Clock pin
    const uint SDIO_DATA0_PIN = 9; // Data pin 0
    const uint SDIO_DATA1_PIN = 4; // Data pin 1
    const uint SDIO_DATA2_PIN = 5; // Data pin 2
    const uint SDIO_DATA3_PIN = 6; // Data pin 3

    gpio_init(SDIO_CMD_PIN);
    gpio_set_dir(SDIO_CMD_PIN, GPIO_OUT);
    gpio_put(SDIO_CMD_PIN, 0); // Command line low initially

    gpio_init(SDIO_CLK_PIN);
    gpio_set_dir(SDIO_CLK_PIN, GPIO_OUT);
    gpio_put(SDIO_CLK_PIN, 0); // Clock line low initially

    gpio_init(SDIO_DATA0_PIN);
    gpio_set_dir(SDIO_DATA0_PIN, GPIO_OUT);

    gpio_init(SDIO_DATA1_PIN);
    gpio_set_dir(SDIO_DATA1_PIN, GPIO_OUT);

    gpio_init(SDIO_DATA2_PIN);
    gpio_set_dir(SDIO_DATA2_PIN, GPIO_OUT);

    gpio_init(SDIO_DATA3_PIN);
    gpio_set_dir(SDIO_DATA3_PIN, GPIO_OUT);
    sleep_ms(2000);

    while (true) {
        // Host sends integers from 0 to 9
        for (int i = 0; i <= 15; ++i) {
            gpio_put(SDIO_CMD_PIN, 1); // Command line high for character transmission start

            // Set 4-bit data on data pins
            gpio_put(SDIO_DATA0_PIN, (i >> 0) & 1);  // bit 0
            gpio_put(SDIO_DATA1_PIN, (i >> 1) & 1);  // bit 1
            gpio_put(SDIO_DATA2_PIN, (i >> 2) & 1);  // bit 2
            gpio_put(SDIO_DATA3_PIN, (i >> 3) & 1);  // bit 3

            // Generate clock pulse
            gpio_put(SDIO_CLK_PIN, 1);
            sleep_ms(50); // Clock pulse duration 
            gpio_put(SDIO_CLK_PIN, 0);
            sleep_ms(50); // Clock pulse duration

            gpio_put(SDIO_CMD_PIN, 0); // Command line low for character transmission end

            // Toggle an LED to indicate character transmission
            gpio_put(LED_PIN, 1);
            sleep_ms(1000);
            gpio_put(LED_PIN, 0);

            // Delay before sending the next character
            sleep_ms(2000);
        }
    }

    return 0;
}
