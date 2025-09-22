connect an esp32 to an oled display where SDA -> 14, and SCL goes to 15.\n
\n
import quadrupy\n
\n
quadrupy.led(BOOLEAN)\n
quadrupy.writeScreen(STRING)\n
quadrupy.clearScreen(NULL)\n
quadrupy.close()\n
\n
programs should always end in quadrupy.close()\n
programs should always clear the screen before exit.\n
\n
you can also use time.sleep(INT) to wait before each command.\n