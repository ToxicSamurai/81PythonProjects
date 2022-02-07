# This program uses a multiline string as a bitmap, a 2D image with only two possible colors for each pixel, to determine how it should display a message from the user.
# In this bitmap, space characters represent an empty space, and all other characters are replaced by characters in the user's message.
# The provided bitmap resembles a world map, but you can change this to any image you'd like.
# The binary simplicity of the space-or-message-characters system makes it good for beginners.

import sys

# (! Try changing this multiline string to another shape !)

bitmap = '''
....................................................................
   **************   *  *** **  *      ******************************
  ********************* ** ** *  * ****************************** *
 **      *****************       ******************************
          *************          **  * **** ** ************** *
           *********            *******   **************** * *
            ********           ***************************  *
   *        * **** ***         *************** ******  ** *
               ****  *         ***************   *** ***  *
                 ******         *************    **   **  *
                 ********        *************    *  ** ***
                   ********         ********          * *** ****
                   *********         ******  *        **** ** * **
                   *********         ****** * *           *** *   *
                     ******          ***** **             *****   *
                     *****            **** *            ********
                    *****             ****              *********
                    ****              **                 *******   *
                    ***                                       *    *
                    **       *                    *
....................................................................
'''

print('Bitmap Message, by Al Sweigart, recreated by Scarlett Wright')
print('Enter the message to display with the bitmap.')

#Sets the message to '> '
message = input('> ')
#If the message = '', exit
if message == '':
    sys.exit()

# Loops over each line in the bitmap:
for line in bitmap.splitlines():
    # Loops over each character in the line:
    for i, bit in enumerate(line):
        if bit == ' ':
            # Prints an empty space since there's a space in the bitmap:
            print(' ', end='')
        else:
            # Print a character from the message:
            print(message[i % len(message)], end='')
    # Prints a newline
    print()