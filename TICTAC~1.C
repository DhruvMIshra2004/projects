#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <graphics.h>
#include <string.h>
#include <time.h>
#include <dos.h>
 
#define d 35                //d=distance
#define s 30                //s=size
#define f 200               //f=display coordinate factor
#define mx getmaxx()
#define my getmaxy()
 
char grid[3][3];
 
int getkey();               //To capture arrow keys pressed
void display(int,int);      //To display grid
int checkWin(int,int,int);  //Check win; return 1 if any one of two players win else 0
int checkDraw(int,int);     //Check draw; return 1 if draw else 0
void end(char *);           //Game end
 
void main()
{
    int gd,gm,sx=0,sy=0,i,j,k,count=2,player;
    char str[25],ch;
 
    detectgraph(&gd,&gm);
    initgraph(&gd,&gm,"C:\\TC\\BGI");
 
    for(i=0;i<3;i++)                            //Initialize grid with blank spaces
        for(j=0;j<3;j++)
            grid[i][j]=' ';
 
    settextstyle(DEFAULT_FONT,HORIZ_DIR,2);     //Initialize text style
 
    while(1)
    {
        cleardevice();
        //Print TIC-TAC-T   OE on screen
        setcolor(BLUE);
        outtextxy(200,150,"TIC-TAC-TOE");
        //Print current Player number
        player=count%2;
        sprintf(str,"Player : %d (%c)",player+1,player?'O':'X');
        setcolor(WHITE);
        outtextxy(350,250,str);
        display(sx,sy);
        ch=getkey();            //Capture arrow key input
        switch(ch)
        {
            case 72:            //up arrow
                if(sy!=0)
                    sy--;
                break;
            case 80:            //down arrow
                if(sy!=2)
                    sy++;
                break;
            case 75:            //left arrow
                if(sx!=0)
                    sx--;
                break;
            case 77:            //right arrow
                if(sx!=2)
                    sx++;
                break;
            case ' ':           //Space key
                if(grid[sy][sx]==' ')       //Mark the cell only if it is empty
                {
                    if(player==0)
                        grid[sy][sx]='X';
                    else
                        grid[sy][sx]='O';
                    count++;
                }
                break;
            case 'e':
            case 'E':       //'e' or 'E' key
                cleardevice();
                closegraph();
                return;
            default :
                break;
        }
        if(checkWin(sx,sy,player)==1||checkDraw(sx,sy)==1)
            break;
    }
    return;
}
 
int getkey()
{
    int ch;
    ch=getch();
    if(ch==0)
    {
        ch=getch();
        return(ch);
    }
    return(ch);
}
 
void display(int sx,int sy)
{
    int i,j;
    char str[2];
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        {
            if(j==sx&&i==sy)                            //If the cell is selected cell
                setcolor(RED);
            else
                setcolor(WHITE);                        //For non-selected cell
            rectangle(j*d+f,i*d+f,j*d+s+f,i*d+s+f);
            sprintf(str,"%c",grid[i][j]);               //To print Player's symbol in cell
            outtextxy(j*d+8+f,i*d+8+f,str);
        }
    }
}
 
int checkWin(int sx,int sy,int player)
{
    char str[25];
    int i,j;
    for(i=0;i<3;i++)
    {
        if((grid[i][0]==grid[i][1]&&grid[i][0]==grid[i][2]&&grid[i][0]!=' ')||(grid[0][i]==grid[1][i]&&grid[0][i]==grid[2][i]&&grid[0][i]!=' '))
        {
            display(sx,sy);
            getch();
            sprintf(str,"Player %d (%c) You Won!!!",player+1,player?'O':'X');
            end(str);
            return(1);
        }
        if((grid[0][0]==grid[1][1]&&grid[1][1]==grid[2][2]&&grid[2][2]!=' ')||(grid[0][2]==grid[1][1]&&grid[1][1]==grid[2][0]&&grid[2][0]!=' '))
        {
            display(sx,sy);
            getch();
            sprintf(str,"Player %d (%c) You Won!!!",player+1,player?'O':'X');
            end(str);
            return(1);
        }
    }
    return(0);
}
 
int checkDraw(int sx,int sy)
{
    int i,j,k=0;
    char str[25];
    for(i=0;i<3;i++)
        for(j=0;j<3;j++)
            if(grid[i][j]!=' ')
                k++;
    if(k==9)        //All cells marked but yet no win i.e. Draw
    {
        display(sx,sy);
        getch();
        sprintf(str,"The game is draw!!!");
        end(str);
        return(1);
    }
    return(0);
}

void end(char *str)
{
    int i,j;
    delay(800);
    cleardevice();
    setcolor(WHITE);
    outtextxy(mx/2-150,my/2,str);
    for(i=0,j=0;i<14;i++){
	    j=1;
	setcolor(j);
	sound(200*j);
	circle(mx/2,my/2,i);
	delay(100);
    }
    nosound();
    outtextxy(mx/2-150,my/2,str);
    getch();
    closegraph();
    return;
}