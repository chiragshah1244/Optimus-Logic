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
    gpio_set_dir(SDIO_CMD_PIN, GPIO_IN);
    gpio_pull_up(SDIO_CMD_PIN);

    gpio_init(SDIO_CLK_PIN);
    gpio_set_dir(SDIO_CLK_PIN, GPIO_IN);
    gpio_pull_up(SDIO_CLK_PIN);

    gpio_init(SDIO_DATA0_PIN);
    gpio_set_dir(SDIO_DATA0_PIN, GPIO_IN);
    gpio_pull_up(SDIO_DATA0_PIN);

    gpio_init(SDIO_DATA1_PIN);
    gpio_set_dir(SDIO_DATA1_PIN, GPIO_IN);
    gpio_pull_up(SDIO_DATA1_PIN);

    gpio_init(SDIO_DATA2_PIN);
    gpio_set_dir(SDIO_DATA2_PIN, GPIO_IN);
    gpio_pull_up(SDIO_DATA2_PIN);

    gpio_init(SDIO_DATA3_PIN);
    gpio_set_dir(SDIO_DATA3_PIN, GPIO_IN);
    gpio_pull_up(SDIO_DATA3_PIN);

    while (true) {
        // Wait for a high clock pulse
        while (!gpio_get(SDIO_CLK_PIN)) {
            sleep_us(10);
        }

        // Receive 4-bit data on data pins
        uint8_t receivedData = 0;
        receivedData |= (gpio_get(SDIO_DATA0_PIN) << 0);
        receivedData |= (gpio_get(SDIO_DATA1_PIN) << 1);
        receivedData |= (gpio_get(SDIO_DATA2_PIN) << 2);
        receivedData |= (gpio_get(SDIO_DATA3_PIN) << 3);

        // LED on when data is received
        if (receivedData != 0) {
            gpio_put(LED_PIN, 1);
        } else {
            gpio_put(LED_PIN, 0);
        }

        // Print received data to the serial monitor
        printf("Received Data: %d\n", receivedData);

        // Wait for falling edge of clock pulse
        while (gpio_get(SDIO_CLK_PIN)) {
            sleep_us(10);
        }
    }

    return 0;
}
