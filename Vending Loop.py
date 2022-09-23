# -*- coding: utf-8 -*-
"""
Created on Sat Jan  2 13:48:10 2021

@author: Garv
"""
#before running code please install easygui
#please check the image directory in line:19,35,63,92,121,150
import easygui
cost_mints=10
cost_chips=15
cost_dew=45
cost_snickers=10
cost_water=20
while 1>0:
    msg="Hello Welcome To Vending Machine, would you like to buy something ?"
    title="Vending Machine - Welcome"
    choices=['Continue','Exit']
    myChoice=easygui.ynbox(msg,title,choices)

    if myChoice==1:
        msg1="What would you like to purchase?"
        title1="Vending Machine - Product Select"
        Choices1=['Mints','Uncle Chips','Mountain Dew','Snickers','Mineral Water']
        choice=easygui.indexbox(msg1,title1,Choices1)
        if choice==0:
            #msg3="Enter quantity: "
            #title3="Vending Machine"
            #d_int = 1
            #Number=easygui.integerbox(msg3,title3,d_int,lowerbound=1,upperbound=5)
            #print(Number)
            purchasePrice=cost_mints
            msg4="Your Bill amount is ₹"+str(purchasePrice)+ " \nPlease deposit Money for purchasing Mints"
            title4="Vending Machine - Insert Money"
            moneyDeposited=easygui.integerbox(msg4,title4,image='D:\Documents\PYTHON\mints.png')
            print(moneyDeposited)
            
            print(purchasePrice)
            if moneyDeposited:
                change= float(moneyDeposited) - purchasePrice 
                print(change)
                if change>=0:
                    msg7="Thank you for your purchase, you change is ₹"+str(change)
                    title7="Vending Machine - Changes"
                    easygui.msgbox(msg7,title7,ok_button='OK')
                else:
                    msg5="You didn't deposit enough money, Please begin again"
                    title5="Vending Machine"
                    easygui.msgbox(msg5,title5,ok_button='OK')
            else:
                msg55="Oops!! Please begin again"
                title55="Vending Machine"
                easygui.msgbox(msg55,title55,ok_button='OK')
        if choice==1:
            #msg3="Enter quantity: "
            #title3="Vending Machine"
            #d_int=1
            #Number=easygui.integerbox(msg3,title3,d_int,lowerbound=1,upperbound=5)
            #print(Number)
            purchasePrice=cost_chips
            msg4="Your Bill amount is ₹"+str(purchasePrice)+ "\nPlease deposit Money for purchasing Uncle Chips"
            title4="Vending Machine - Insert Money"
            moneyDeposited=easygui.integerbox(msg4,title4,image='D:\Documents\PYTHON\chips.png')
            print(moneyDeposited)
            
            print(purchasePrice)
            if moneyDeposited:
                change= float(moneyDeposited) - purchasePrice 
                print(change)
                if change>=0:
                    msg7="Thank you for your purchase, you change is ₹"+str(change)
                    title7="Vending Machine - Changes" 
                    easygui.msgbox(msg7,title7,ok_button='OK')
                else:
                    msg5="You didn't deposit enough money, Please begin again"
                    title5="Vending Machine"
                    easygui.msgbox(msg5,title5,ok_button='OK')
            else:
                msg55="Oops!! Please begin again"
                title55="Vending Machine"
                easygui.msgbox(msg55,title55,ok_button='OK')
    
        if choice==2:
            #msg3="Enter quantity: "
            #title3="Vending Machine"
            #d_int=1
            #Number=easygui.integerbox(msg3,title3,d_int,lowerbound=1,upperbound=5)
            #print(Number)
            purchasePrice=cost_dew
            msg4="Your Bill amount is ₹"+str(purchasePrice)+ "\nPlease deposit Money for purchasing Mountain Dew"
            title4="Vending Machine - Insert Money"
            moneyDeposited=easygui.integerbox(msg4,title4,image='D:\Documents\PYTHON\dew.png')
            print(moneyDeposited)
             
            print(purchasePrice)
            if moneyDeposited:
                change= float(moneyDeposited) - purchasePrice 
                print(change)
                if change>=0:
                    msg7="Thank you for your purchase, you change is ₹"+str(change)
                    title7="Vending Machine - Changes"
                    easygui.msgbox(msg7,title7,ok_button='OK')
                else:
                    msg5="You didn't deposit enough money, Please begin again"
                    title5="Vending Machine"
                    easygui.msgbox(msg5,title5,ok_button='OK')
            else:
                msg55="Oops!! Please begin again"
                title55="Vending Machine"
                easygui.msgbox(msg55,title55,ok_button='OK')
                
        if choice==3:
            #msg3="Enter quantity: "
            #title3="Vending Machine"
            #d_int=1
            #Number=easygui.integerbox(msg3,title3,d_int,lowerbound=1,upperbound=5)
            #print(Number)
            purchasePrice=cost_snickers 
            msg4="Your Bill amount is ₹"+str(purchasePrice)+ "\nPlease deposit Money for purchasing Snickers"
            title4="Vending Machine - Insert Money"
            moneyDeposited=easygui.integerbox(msg4,title4,image='D:\Documents\PYTHON\snickers.png')
            print(moneyDeposited)
            
            print(purchasePrice)
            if moneyDeposited:
                change= float(moneyDeposited) - purchasePrice 
                print(change)
                if change>=0:
              
                    msg7="Thank you for your purchase, you change is ₹"+str(change)
                    title7="Vending Machine - Changes"
                    easygui.msgbox(msg7,title7,ok_button='OK')
                else:
                    msg5="You didn't deposit enough money, Please begin again"
                    title5="Vending Machine"
                    easygui.msgbox(msg5,title5,ok_button='OK')
            else:
                msg55="Oops!! Please begin again"
                title55="Vending Machine"
                easygui.msgbox(msg55,title55,ok_button='OK')
        if choice==4:
            #msg3="Enter quantity: "
            #title3="Vending Machine"
            #d_int=1
            #Number=easygui.integerbox(msg3,title3,d_int,lowerbound=1,upperbound=5)
            #print(Number)
            purchasePrice=cost_water 
            msg4="Your Bill amount is ₹"+str(purchasePrice)+ "\nPlease deposit Money for purchasing Mineral Water"
            title4="Vending Machine - Insert Money"
            moneyDeposited=easygui.integerbox(msg4,title4,image='D:\Documents\PYTHON\water.png')
            print(moneyDeposited)
            
            print(purchasePrice)
            if moneyDeposited:
                change= float(moneyDeposited) - purchasePrice 
                print(change)
                if change>=0:
                
                    msg7="Thank you for your purchase, you change is ₹"+str(change)
                    title7="Vending Machine - Changes"
                    easygui.msgbox(msg7,title7,ok_button='OK')
                else:
                    msg5="You didn't deposit enough money, Please begin again"
                    title5="Vending Machine"
                    easygui.msgbox(msg5,title5,ok_button='OK')
            else:
                msg55="Oops!! Please begin again"
                title55="Vending Machine"
                easygui.msgbox(msg55,title55,ok_button='OK')
    else:
        msg2="Thank your for Visiting, Have a good day!"
        title2="Vending Machine - Exit"
        easygui.msgbox(msg2,title2,ok_button='OK')
        break
    