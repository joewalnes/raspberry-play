Demonstrates using a shift register to create a simple animation with 16 LEDs, while only using 3 GPIO pins of the Raspberry Pi.

![Raspberry Pi connected to a shift register](https://p.twimg.com/AtnfdJyCMAADUCw.jpg)

__[Watch a demonstration video](http://elinux.org/Rpi_Low-level_peripherals)__

The example should run on the Raspberry Pi Debian Squeeze distro, with the standard Python and no additional libraries.


Wiring
======

I used the [Texas Instruments TLC5925 Shift Register](http://www.ti.com/product/tlc5925), which I had conveniently mounted on a [breakout board available from SparkFun](http://www.sparkfun.com/products/10407).

Refer to the [eLinux Low Level Peripherals](http://elinux.org/Rpi_Low-level_peripherals) page for pin-out diagrams of the Pi.

Pins:

    Pi         Shift register
    =======    ==============

    # GPIO
    GPIO 17 -> SDI (Data in)
    GPIO 21 -> CLK (Clock)
    GPIO 22 -> LE  (Latch)
    
    # Power
    5V      -> VCC
    Ground  -> Ground

    # In addition, you should connect the TLC5925 OE pin to Ground, to ensure the LEDs are enabled.



Just a demo! Come see more stuff at [quick2wire.com](http://quick2wire.com/)
