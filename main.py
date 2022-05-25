#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import datetime as dt


def add_element(conn):
    name = input('Конечный пункт: ')
    num = input('Номер поезда: ')
    tm = input('Время отправления: ')

    tm = dt.datetime(tm)
    cur = conn.cursor()
    query = f"""
    INSERT INTO citys (id, city)
    VALUES
    ({num}, '{name}');
    
    INSERT INTO train (train_id, time, city)
    VALUES
    ({num}, {tm}, {num})
    """
    cur.execute(query)
    conn.commit()
    cur.close()



def find_train(num, conn):
    cur = conn.cursor()
    query = f"""SELECT *
    FROM train
    JOIN citys ON train.city=citys.id
    WHERE train.train_id = {num}"""
    cur.execute(query)
    res = cur.fetchone()
    cur.close()

    print(
    f'Конечный пункт: {res[2]} \n'
    f'Номер поезда: {res[0]} \n'
    f'Время отправления: {res[1]}'
    )
    return
    print('Поезда с таким номером нет')


if __name__ == '__main__':
    print('LOADING...')
    conn = sqlite3.connect('data.db')
    cur = conn.cursor()
    query = """
    CREATE TABLE IF NOT EXISTS citys(
    id INT PRIMARY KEY,
    city VARCHAR(50));
    
    CREATE TABLE IF NOT EXISTS train(
    train_id INT PRIMARY KEY,
    time DATATIME,
    city INT,
    FOREIGN KEY (city) REFERENCES citys(id));"""

    cur.execute(query)
    conn.commit()
    cur.close()
    print('Hello!')

    flag = True
    while flag:
        print('1. Добавить новый поезд')
        print('2. Вывести информацию о поезде')
        print('3.Выход из программы')
        com = int(input('введите номер команды: '))
        if com == 1:
            add_element(conn)
        elif com == 2:
            train_num = input('Введите номер поезда: ')
            find_train(train_num, conn)
        elif com == 3:
            flag = False
    conn.close()