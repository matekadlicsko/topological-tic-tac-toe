import numpy as np

class top_ttt:

    bold= lambda string:'\033[93m' "\033[1m" + string + "\033[0m" "\033[0m"

    def __init__(self, table):
        self.table=table
        self.height=len(table)
        self.width=len(table[0])

    def modify(self, XO, pos):
        self.table[pos[0]][pos[1]]=XO


    def winning_triple_plane(self):
        T=self.table
        for i in range(self.height):
            for j in range(self.width-2):
                if T[i][j]==T[i][j+1] and T[i][j+1]==T[i][j+2] and T[i][j]!=0:
                    return [[i,j], [i, j+1], [i, j+2]]

        for i in range(self.height-2):
            for j in range(self.width):
                if T[i][j]!=0:
                    if T[i][j]==T[i+1][j] and T[i+1][j]==T[i+2][j]:
                        return [ [i,j],[i+1, j], [i+2,j] ]

        for i in range(self.height-2):
            for j in range(self.width-2):
                if T[i][j]==T[i+1][j+1] and T[i+2][j+2]==T[i+1][j+1] and T[i][j]!=0:
                    return [ [i,j], [i+1,j+1], [i+2,j+2] ]
                elif T[i][self.width -j-1]!=0:
                    if T[i][self.width -j-1]==T[i+1][self.width-j-2] and T[i+1][self.width-j-2]==T[i+2][self.width-j-3]:
                        return [ [i, self.width -j-1], [i+1, self.width-j-2], [i+2, self.width-j-3] ]

        return []

    def winner(self):
        T=self.table
        L=self.winning_triple()

        win=True

        if len(L)==3:
            for i in range(len(L)):
                for j in range(len(L)):
                    if i!=j and L[i]==L[j]:
                        win=False
        else:
            win=False

        if win:
            return T[L[0][0]][L[0][1]]
        else:
            return "none"

    def display_chars(x):
        if x==0:
            return " "
        elif x==1:
            return "X"
        elif x==2:
            return "O"

    def __str__(self):
        T=self.table
        string="     "
        trip=self.winning_triple()

        for i in range(self.width):
            string+=str(i+1)+"   "
        string+="\n   "

        for i in range(self.width):
            string=string+"+---"
        string=string+"+"+"\n"

        win=True
        for i in range(len(trip)):
            for j in range(len(trip)):
                if i!=j and trip[i]==trip[j]:
                    win=False

        for i in range(self.height):
            string=string+str(i+1)+"  |"
            for j in range(self.width):
                if [i,j] in trip and win:
                    string=string+" "+top_ttt.bold(str( top_ttt.display_chars(T[i][j]) ) )+ " |"

                else:
                    string=string+" "+str( top_ttt.display_chars(T[i][j]) )+ " |"

            string=string+"\n"+"   +"
            for j in range(self.width):
                string=string+"---+"
            string=string+"\n"

        return string


class square_ttt(top_ttt):

    def extended_table(self):
        return self.table()

    def winning_triple(self):
        return self.winning_triple_plane()

    def __str__(self):
        return super().__str__()

class torus_ttt(top_ttt):
    def extended_table(self):
        L=[]
        K=[]
        for k in range(self.height):
            L.append([])

        for k in range(self.height):
            for i in range(3):
                for j in range(self.width):
                    L[k].append(self.table[k][j])

        for i in range(3):
            for x in L:
                K.append(x)

        return K

    def winning_triple(self):
        L=self.extended_table()
        T=square_ttt(L)
        trip=T.winning_triple_plane()
        for t in trip:
            t[0]=t[0]%self.height
            t[1]=t[1]%self.width
        return trip

    def __str__(self):
        T=self.table
        string="     "
        trip=self.winning_triple()

        for i in range(self.width):
            string+=str(i+1)+"   "
        string+="\n   "

        for i in range(self.width):
            string=string+"+---"
        string=string+"+"+"\n"

        win=True
        for i in range(len(trip)):
            for j in range(len(trip)):
                if i!=j and trip[i]==trip[j]:
                    win=False

        for i in range(self.height):
            string=string+str(i+1)+"  |"
            for j in range(self.width):
                if [i,j] in trip and win:
                    string=string+" "+top_ttt.bold(str( top_ttt.display_chars(T[i][j]) ) )+ " |"

                else:
                    string=string+" "+str( top_ttt.display_chars(T[i][j]) )+ " |"

            string=string+ " " + str(i+1) +"\n"+"   +"
            for j in range(self.width):
                string=string+"---+"
            string=string+"\n"

        string+="     "

        for i in range(self.width):
            string+=str(i+1)+"   "

        return string

class cylinder_ttt(top_ttt):


    def extended_table(self):
        L=[]

        for k in range(self.height):
            L.append([])

        for k in range(self.height):
            for i in range(3):
                for j in range(self.width):
                    L[k].append(self.table[k][j])
        return L

    def winning_triple(self):
        L=self.extended_table()
        T=square_ttt(L)
        trip=T.winning_triple_plane()
        for t in trip:
            t[1]=t[1]%self.width

        return trip

    def __str__(self):
        T=self.table
        string="     "
        trip=self.winning_triple()

        for i in range(self.width):
            string+=str(i+1)+"   "
        string+="\n   "

        for i in range(self.width):
            string=string+"+---"
        string=string+"+"+"\n"

        win=True
        for i in range(len(trip)):
            for j in range(len(trip)):
                if i!=j and trip[i]==trip[j]:
                    win=False

        for i in range(self.height):
            string=string+str(i+1)+"  |"
            for j in range(self.width):
                if [i,j] in trip and win:
                    string=string+" "+top_ttt.bold(str( top_ttt.display_chars(T[i][j]) ) )+ " |"

                else:
                    string=string+" "+str( top_ttt.display_chars(T[i][j]) )+ " |"

            string=string+ " " + str(i+1) +"\n"+"   +"
            for j in range(self.width):
                string=string+"---+"
            string=string+"\n"

        return string

class mobius_ttt(top_ttt):
    def extended_table(self):
        L=list(self.table)
        L.reverse()

        K=[]

        for i in range(self.height):
            K.append([])
            K[i].extend(L[i])
            K[i].extend(self.table[i])
            K[i].extend(L[i])
        return K

    def winning_triple(self):
        L=self.extended_table()
        T=square_ttt(L)
        trip=T.winning_triple_plane()

        for t in trip:
            if t[1]<=self.width - 1:
                t[1]= t[1] %self.width
                t[0]= self.height-t[0]-1
            elif t[1]<=2*self.width -1:
                t[1]=t[1]%self.width
            else:
                t[1]=t[1]%self.width
                t[0]= self.height-t[0]-1
        return trip

    def __str__(self):
        T=self.table
        string="     "
        trip=self.winning_triple()

        for i in range(self.width):
            string+=str(i+1)+"   "
        string+="\n   "

        for i in range(self.width):
            string=string+"+---"
        string=string+"+"+"\n"

        win=True
        for i in range(len(trip)):
            for j in range(len(trip)):
                if i!=j and trip[i]==trip[j]:
                    win=False

        for i in range(self.height):
            string=string+str(i+1)+"  |"
            for j in range(self.width):
                if [i,j] in trip and win:
                    string=string+" "+top_ttt.bold(str( top_ttt.display_chars(T[i][j]) ) )+ " |"

                else:
                    string=string+" "+str( top_ttt.display_chars(T[i][j]) )+ " |"

            string=string+ " " + str(self.height - i) +"\n"+"   +"
            for j in range(self.width):
                string=string+"---+"
            string=string+"\n"

        return string

class klein_ttt(top_ttt):
    def extended_table(self):
        L=list(self.table)
        L.reverse()

        K=[]

        for i in range(self.height):
            K.append([])
            K[i].extend(L[i])
            K[i].extend(self.table[i])
            K[i].extend(L[i])
        L=[]

        for i in range(3):
            for x in K:
                L.append(x)

        return L

    def winning_triple(self):
        L=self.extended_table()
        T=square_ttt(L)
        trip=T.winning_triple_plane()
        for t in trip:
            if t[1]<=self.width - 1:
                t[1]= t[1] %self.width
                t[0]= self.height-t[0]-1
            elif t[1]<=2*self.width -1:
                t[1]=t[1]%self.width
            else:
                t[1]=t[1]%self.width
                t[0]= self.height-t[0]-1

            t[0]=t[0]%self.height
        return trip


    def __str__(self):
        T=self.table
        string="     "
        trip=self.winning_triple()

        for i in range(self.width):
            string+=str(i+1)+"   "
        string+="\n   "

        for i in range(self.width):
            string=string+"+---"
        string=string+"+"+"\n"

        win=True
        for i in range(len(trip)):
            for j in range(len(trip)):
                if i!=j and trip[i]==trip[j]:
                    win=False

        for i in range(self.height):
            string=string+str(i+1)+"  |"
            for j in range(self.width):
                if [i,j] in trip and win:
                    string=string+" "+top_ttt.bold(str( top_ttt.display_chars(T[i][j]) ) )+ " |"

                else:
                    string=string+" "+str( top_ttt.display_chars(T[i][j]) )+ " |"

            string=string+ " " + str(self.height - i) +"\n"+"   +"
            for j in range(self.width):
                string=string+"---+"
            string=string+"\n"

        string+="     "

        for i in range(self.width):
            string+=str(i+1)+"   "


        return string


class projective_plane_ttt(top_ttt):

    def extended_table(self):
        L=list(self.table)
        L.reverse()

        K=[]

        for i in range(self.height):
            K.append([])
            K[i].extend(L[i])
            K[i].extend(self.table[i])
            K[i].extend(L[i])
        L1=[]

        for x in K:
            L1.append(x)
        L2=[]
        for x in L1:
            L2.append(list(x))

        for x in L2:
            x.reverse()

        LFinal=[]

        for x in L2:
            LFinal.append(x)
        for x in L1:
            LFinal.append(x)
        for x in L2:
            LFinal.append(x)
        return LFinal

    def __str__(self):
        T=self.table
        string="     "
        trip=self.winning_triple()

        for i in range(self.width):
            string+=str(i+1)+"   "
        string+="\n   "

        for i in range(self.width):
            string=string+"+---"
        string=string+"+"+"\n"

        win=True
        for i in range(len(trip)):
            for j in range(len(trip)):
                if i!=j and trip[i]==trip[j]:
                    win=False

        for i in range(self.height):
            string=string+str(i+1)+"  |"
            for j in range(self.width):
                if [i,j] in trip and win:
                    string=string+" "+top_ttt.bold(str( top_ttt.display_chars(T[i][j]) ) )+ " |"

                else:
                    string=string+" "+str( top_ttt.display_chars(T[i][j]) )+ " |"

            string=string+ " " + str(self.height - i) +"\n"+"   +"
            for j in range(self.width):
                string=string+"---+"
            string=string+"\n"

        string+="     "

        for i in range(self.width):
            string+=str(self.width-i)+"   "


        return string


    def winning_triple(self):
        L=self.extended_table()
        T=square_ttt(L)
        trip=T.winning_triple_plane()
        for t in trip:
            if t[0]>=self.height and t[0]<=2*self.height-1:
                if t[0]>=self.width and t[0]<=2*self.width-1:
                    t[0]=t[0]%self.height
                    t[1]=t[1]%self.width
                else:
                    t[0]=t[0]%self.height
                    t[1]=t[1]%self.width
                    t[0]=self.height - t[0]-1
            else:
                if t[0]>=self.width and t[0]<=2*self.width-1:
                    t[0]=t[0]%self.height
                    t[1]=t[1]%self.width
                    t[1]=self.width-t[1]
                else:
                    t[0]=t[0]%self.height
                    t[1]=t[1]%self.width
                    t[0]=self.height - t[0]-1
                    t[1]=self.width - t[1]-1

        return trip


def game():

    print("sorok száma:")
    n=int(input())
    print("oszlopok száma")
    m=int(input())

    M=[0 for i in range(n*m)]
    M=np.matrix(M).reshape(n, m).tolist()
    print("válassz topologikus teret:")
    print("1=square, 2=mobius strip, 3=cylinder, 4=projective plane, 5=klein bottle, 6=torus")

    while(True):
        topology=input()
        if topology=="1":
            T=square_ttt(M)
            break
        elif topology=="2":
            T=mobius_ttt(M)
            break
        elif topology=="3":
            T=cylinder_ttt(M)
            break
        elif topology=="4":
            T=projective_plane_ttt(M)
            break
        elif topology=="5":
            T=klein_ttt(M)
            break
        elif topology=="6":
            T=torus_ttt(M)
            break
        else:
            print("egy 1 és 6 közötti egész számot adj meg")
            topology=input()

    print("...kezdődik....")
    print(T)

    while(True):
        while(True):
            print("X köre:")
            print("sor:")
            sorX=int(input())-1

            while(type(sorX)!=int):
                print("egész számot adj meg")
                sorX=int(input())-1

            while(sorX<0 or sorX>T.height -1 ):
                print("korlátokon kívüli szám")
                sorX=int(input())-1

            print("oszlop:")
            oszlopX=int(input())-1

            while(type(oszlopX)!=int):
                print("egész számot adj meg")
                oszlopX=int(input())-1

            while(oszlopX<0 or oszlopX>T.width -1 ):
                print("korlátokon kívüli szám")
                oszlopX=int(input())-1

            if T.table[sorX][oszlopX]==0:
                T.modify(1, [sorX, oszlopX])
                print(T)
                break
            else:
                print("idióta")

        if T.winner()!="none":
            print("A nyertes: ")
            print(top_ttt.display_chars(T.winner()))
            return 0

        no0=0
        for x in T.table:
            for y in x:
                if y==0:
                    no0+=1
        if no0==0:
            print("döntetlen")
            return 0

        while(True):
            print("O köre:")
            print("sor:")
            sorY=int(input())-1
            print("oszlop:")
            oszlopY=int(input())-1

            if T.table[sorY][oszlopY]==0:
                T.modify(2, [sorY, oszlopY])
                print(T)
                break
            else:
                print("idióta")

        if T.winner()!="none":
            print("A nyertes: ")
            print(top_ttt.display_chars(T.winner()))
            return 0

        no0=0
        for x in T.table:
            for y in x:
                if y==0:
                    no0+=1
        if no0==0:
            print("döntetlen")
            return 0

    return 0

game()
