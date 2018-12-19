from cryptoline_modules import decode_cipher as dc


def main():
    draw_logo()
    print("Enter a cryptogram to decode:", end=" ")

    entry = input()
    list = [entry]
    print("Possible results:")
    dc.decode_multilayer(list, 3)




def draw_logo():
    logo =  """                             __         .__  .__               
  ___________ ___.__._______/  |_  ____ |  | |__| ____   ____  
_/ ___\_  __ <   |  |\____ \   __\/  _ \|  | |  |/    \_/ __ \ 
\  \___|  | \/\___  ||  |_> >  | (  <_> )  |_|  |   |  \  ___/ 
 \___  >__|   / ____||   __/|__|  \____/|____/__|___|  /\___  >
     \/       \/     |__|                            \/     \/ 
    """

    print(logo)


if __name__ == '__main__':
    main()
