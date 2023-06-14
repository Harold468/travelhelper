import googlemaps
from tkinter import *
from tkinter import ttk
import tkintermapview
from tkinter import messagebox

def showinfos():
    messagebox.showinfo('Information about searched location',f'origin:{str(origin).lower()}\n destination:{str(destination).lower()}')

def show_map():
    try:
        if(origintext.get()!='' and destinationtext.get()!=''):
            gmaps = googlemaps.Client(key='AIzaSyAiM_lnecaPtWzId9aBml5l1tdGL2zpnCM')
            results = gmaps.distance_matrix(
            str(origintext.get()).lower(),str(destinationtext.get()).lower(),
            mode=mode_of_transport.get()
            )
            print(results)
            map_widget = tkintermapview.TkinterMapView(root, width=700, height=400, corner_radius=20)
            map_widget.place(relx=0.5, rely=0.6, anchor=CENTER)

            marker_1 = map_widget.set_address(str(origintext.get()).lower(), marker=True)
            marker_1.set_text('Origin')

            marker_2 = map_widget.set_address(str(destinationtext.get()).lower(), marker=True)
            marker_2.set_text('Destination')

            path_1 = map_widget.set_path([marker_1.position, marker_2.position],width=3)

            l4=Label(frame1,fg='maroon',bg='skyblue',
                    font=('Times',22,'bold'),
                    text='Results'
                    )

            originslabel=f'origin: {str(origintext.get()).lower()}'
            
            l5.config(text=originslabel)

            originslabel=f'destination: {str(destinationtext.get()).lower()}'

            l6.config(text=originslabel)

            distanceinfo='Distance is: ' + str(results['rows'][0]['elements'][0]['distance']['text'])

            l7.config(text=distanceinfo)


            infotime='Time is: ' +str(results['rows'][0]['elements'][0]['duration']['text'])


            l8.config(text=infotime)


            messagebox.showinfo('Distance',str(results))
        else:
            messagebox.showerror('Please check for the empty fields','some of the fieds are empty')
    except:
        messagebox.showerror('Distance or Location Error','Location may be too far for the selected mode of travel or the location was not recognized by google')

gmaps = googlemaps.Client(key='AIzaSyAiM_lnecaPtWzId9aBml5l1tdGL2zpnCM')

origin='Kumasi'
destination='AccRA'


mode_of_transport_values=["driving", "walking"]
results = gmaps.distance_matrix(
    str(origin).lower(),str(destination).lower(),
    mode='walking'
    )

root=Tk()
root.geometry('800x600')
root.title('Distance Matrix Api by Dennis Asante')

backgroundimage=PhotoImage(file='backgroundimage.png')
l1=Label(root,bg='skyblue',image=backgroundimage
         )
# l1.place(x=0, y=0, relwidth=1, relheight=1)

l1=Label(root,bg='skyblue',fg='black',
         font=('Times',32,'bold'),
         text='Travel Helper for finding the best route to take and time to spare'
         )
l1.place(relx=0.05,rely=0.01)

frame1 = Frame(root,width=800,height=300)
frame1.config(bg='skyblue')
frame1.place(relx=0.05,rely=0.08)

l2=Label(frame1,fg='maroon',bg='skyblue',
         font=('Times',22,'bold'),
         text='Origin'
         )
l2.grid(row=0,column=0)
origintext=StringVar()
e1 = Entry(frame1,textvariable=origintext,width=10,fg='blue')
origintext.set(origin.lower())
e1.grid(row=1,column=0)

l2=Label(frame1,fg='maroon',bg='skyblue',
         font=('Times',22,'bold'),
         text='Destination'
         )
l2.grid(row=0,column=1)
destinationtext=StringVar()
e1 = Entry(frame1,textvariable=destinationtext,width=10,fg='blue')
e1.grid(row=1,column=1)
destinationtext.set(destination.lower())


l3=Label(frame1,fg='maroon',bg='skyblue',
         font=('Times',22,'bold'),
         text='Mode'
         )
l3.grid(row=0,column=3)
modetext=StringVar()

mode_of_transport=ttk.Combobox(frame1,values=mode_of_transport_values,width=10)
mode_of_transport.config(state='readonly')
mode_of_transport.current(0)
mode_of_transport.grid(row=1,column=3)
print('stuff',mode_of_transport.get())

btn1 = Button(frame1,text='GO',font=('Times',32,'bold'),bg='blue',fg='maroon',activebackground='gold',command=show_map)
btn1.grid(row=0,column=4)

l4=Label(frame1,fg='maroon',bg='skyblue',
         font=('Times',22,'bold'),
         text='Results'
         )
l4.grid(row=0,column=5)

originslabel=f'origin: {str(origin).lower()}'
l5=Label(frame1,bg='skyblue',
         font=('Times',22,'bold'),
         text=originslabel
         )
l5.grid(row=1,column=5)

originslabel=f'destination: {str(destination).lower()}'
l6=Label(frame1,bg='skyblue',
         font=('Times',22,'bold'),
         text=originslabel
         )
l6.grid(row=2,column=5)

distanceinfo='Distance is: ' + str(results['rows'][0]['elements'][0]['distance']['text'])
l7=Label(frame1,bg='skyblue',
         font=('Times',20,'bold'),
         text=distanceinfo
         )
l7.grid(row=0,column=6)


infotime='Time is: ' +str(results['rows'][0]['elements'][0]['duration']['text'])
l8=Label(frame1,bg='skyblue',
         font=('Times',20,'bold'),
         text=infotime
         )
l8.grid(row=1,column=6)


map_widget = tkintermapview.TkinterMapView(root, width=700, height=400, corner_radius=5)
map_widget.place(relx=0.5, rely=0.6, anchor=CENTER)
marker_1 = map_widget.set_address(str(origin).lower(), marker=True)
marker_1.set_text('Origin')
marker_2 = map_widget.set_address(str(destination).lower(), marker=True)
marker_2.set_text('Destination')
path_1 = map_widget.set_path([marker_1.position, marker_2.position],width=3)

print(results['destination_addresses'])
print(results['origin_addresses'])
print(results['rows'][0]['elements'][0]['distance']['text'])
print(results['rows'][0]['elements'][0]['duration']['text'])

if __name__ =='__main__':
    root.mainloop()