# -*- coding: utf-8 -*-
"""
===============================================================================
🐍 PCEP GEHIRN-TRAINER ULTIMATE – KOHLENSTOFFEINHEITEN-EDITION (200 FRAGEN)
===============================================================================
Desktop-App (Python / Tkinter) – 100% Standardbibliothek (kein pip nötig!)
Starten mit:
    python pcep_quiz_app.py
===============================================================================
"""

import tkinter as tk
from tkinter import messagebox
import random
import json
from pathlib import Path

BANK = [{'b': 1, 'code': 'print(7 / 7)', 'p': 'What is the output of the following code?', 'o': ['1', '1.0', '7/7', 'Error'], 'a': 1, 'kid': "Der Schrägstrich / ist ein Zauberer, der IMMER eine Kommazahl rausspuckt – auch wenn's glatt aufgeht.", 'tech': '/ ist die echte Division und liefert in Python 3 immer float. 7/7 → 1.0', 'trap': True, 'run': True, 'v': 'both', 'id': 0, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(7 // 2)', 'p': 'What is the output of the following code?', 'o': ['3.5', '3', '4', '3.0'], 'a': 1, 'kid': '// heißt: teilen und alles hinter dem Komma wegschmeißen. 7 Bonbons auf 2 Kinder = jeder 3 ganze.', 'tech': '// ist Floor-Division. Bei zwei ints kommt int raus: 3.', 'trap': False, 'run': True, 'v': 'both', 'id': 1, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(-7 // 2)', 'p': 'What is the output of the following code?', 'o': ['-3', '-4', '-3.5', '3'], 'a': 1, 'kid': '// rundet immer NACH UNTEN auf dem Zahlenstrahl – und unter -3.5 liegt -4, nicht -3!', 'tech': 'Floor-Division rundet Richtung minus unendlich: floor(-3.5) = -4.', 'trap': True, 'run': True, 'v': 'both', 'id': 2, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(7 % 3)', 'p': 'What is the output of the following code?', 'o': ['2', '1', '0', '2.33'], 'a': 1, 'kid': '% ist der Rest-Detektiv: 7 Kekse, immer 3er-Päckchen → 1 Keks bleibt übrig.', 'tech': 'Modulo liefert den Rest der Ganzzahldivision: 7 = 2*3 + 1.', 'trap': False, 'run': True, 'v': 'both', 'id': 3, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(-7 % 3)', 'p': 'What is the output of the following code?', 'o': ['-1', '1', '2', '-2'], 'a': 2, 'kid': 'Bei % hat der Rest immer das Vorzeichen der RECHTEN Zahl. Rechts steht 3 (positiv), also ist der Rest positiv: 2.', 'tech': 'a % b = a - b*(a//b) = -7 - 3*(-3)... genauer: -7//3 = -3 → -7 - (-9) = 2.', 'trap': True, 'run': True, 'v': 'both', 'id': 4, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(2 ** 3 ** 2)', 'p': 'What is the output of the following code?', 'o': ['64', '512', '36', '12'], 'a': 1, 'kid': '** ist der einzige Rebell, der von RECHTS nach links rechnet: erst 3**2 = 9, dann 2**9 = 512.', 'tech': 'Der Potenzoperator ist rechtsassoziativ: 2 ** (3 ** 2) = 2 ** 9 = 512.', 'trap': True, 'run': True, 'v': 'both', 'id': 5, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(-2 ** 2)', 'p': 'What is the output of the following code?', 'o': ['4', '-4', '0.25', 'Error'], 'a': 1, 'kid': 'Erst wird potenziert (2**2 = 4), DANN kommt das Minus davor. Das Minus ist zu langsam!', 'tech': '** bindet stärker als das unäre Minus links davon: -(2**2) = -4.', 'trap': True, 'run': True, 'v': 'both', 'id': 6, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(2 ** -1)', 'p': 'What is the output of the following code?', 'o': ['-2', '0.5', 'Error', '0'], 'a': 1, 'kid': 'Hoch minus 1 heißt: 1 geteilt durch die Zahl. 1/2 = 0.5.', 'tech': 'Negativer Exponent → Kehrwert, Ergebnis ist float: 0.5.', 'trap': False, 'run': True, 'v': 'both', 'id': 7, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(0b101 + 0o10 + 0x1)', 'p': 'What is the output of the following code?', 'o': ['111', '14', '12', 'Error'], 'a': 1, 'kid': '0b = Binär (101 = 5), 0o = Oktal (10 = 8), 0x = Hexadezimal (1 = 1). 5 + 8 + 1 = 14.', 'tech': 'Präfixe: 0b binär, 0o oktal, 0x hex. print zeigt immer dezimal.', 'trap': False, 'run': True, 'v': 'both', 'id': 8, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(1e3)', 'p': 'What is the output of the following code?', 'o': ['1000', '1000.0', '1e3', '3'], 'a': 1, 'kid': '1e3 heißt 1 mal 10 hoch 3. Und alles mit e ist automatisch eine Kommazahl.', 'tech': 'Wissenschaftliche Notation erzeugt immer float: 1000.0.', 'trap': True, 'run': True, 'v': 'both', 'id': 9, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print("a", "b", "c", sep="-", end="!")', 'p': 'What is the output of the following code?', 'o': ['a-b-c!', 'a b c!', '-a-b-c!', 'abc-!'], 'a': 0, 'kid': 'sep ist der Kleber ZWISCHEN den Sachen, end ist das, was ganz am Schluss kommt.', 'tech': "sep trennt die Argumente (Standard ' '), end ersetzt das '\\n' am Ende.", 'trap': False, 'run': True, 'v': 'both', 'id': 10, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print("Hi", end="")\nprint("Ho")', 'p': 'What is the output of the following code?', 'o': ['Hi\nHo', 'HiHo', 'Hi Ho', 'Ho'], 'a': 1, 'kid': 'end="" heißt: KEIN Zeilenumbruch nach \'Hi\'. Also klebt \'Ho\' direkt dran.', 'tech': "Das Standard-end ist '\\n'. Mit end='' bleibt der Cursor in derselben Zeile.", 'trap': False, 'run': True, 'v': 'both', 'id': 11, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(1, 2, sep="")', 'p': 'What is the output of the following code?', 'o': ['1 2', '12', '3', '1,2'], 'a': 1, 'kid': 'sep="" heißt: Kleber ist leer. Die Zahlen kuscheln direkt nebeneinander.', 'tech': "Leerer Separator → '12'. Es wird nichts addiert!", 'trap': False, 'run': True, 'v': 'both', 'id': 12, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'x = input()   # the user types: 5\nprint(x * 2)', 'p': 'What is the output of the following code?', 'o': ['10', '55', 'Error', '5 5'], 'a': 1, 'kid': "input() gibt dir IMMER Text, auch wenn jemand eine Zahl tippt. Text mal 2 = Text doppelt: '55'.", 'tech': "input() liefert str. '5' * 2 = '55'. Für Rechnen: int(input()).", 'trap': True, 'run': False, 'v': 'both', 'id': 13, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(int("3.5"))', 'p': 'What is the output of the following code?', 'o': ['3', '4', '3.5', 'ValueError'], 'a': 3, 'kid': "int() kann Text nur in Ganzzahl verwandeln, wenn da wirklich eine Ganzzahl steht. '3.5' versteht er nicht → Wutanfall.", 'tech': "int('3.5') → ValueError. Erst float('3.5'), dann int() würde gehen.", 'trap': True, 'run': True, 'v': 'both', 'id': 14, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(int(3.99))', 'p': 'What is the output of the following code?', 'o': ['4', '3', '3.99', 'Error'], 'a': 1, 'kid': 'int() rundet nicht, es schneidet einfach ab. Wie eine Schere hinter dem Komma.', 'tech': 'int() auf float schneidet Richtung 0 ab (truncate): 3.', 'trap': False, 'run': True, 'v': 'both', 'id': 15, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(float("3"))', 'p': 'What is the output of the following code?', 'o': ['3', '3.0', "'3'", 'Error'], 'a': 1, 'kid': "float macht aus allem eine Kommazahl, auch aus dem Text '3'.", 'tech': "float('3') → 3.0", 'trap': False, 'run': True, 'v': 'both', 'id': 16, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(True + True)', 'p': 'What is the output of the following code?', 'o': ['TrueTrue', '2', 'True', 'Error'], 'a': 1, 'kid': 'Für Python ist True heimlich eine 1 und False eine 0. 1 + 1 = 2.', 'tech': 'bool ist eine Unterklasse von int: True == 1, False == 0.', 'trap': True, 'run': True, 'v': 'both', 'id': 17, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(5 & 3)', 'p': 'What is the output of the following code?', 'o': ['8', '1', '7', 'True'], 'a': 1, 'kid': '& vergleicht die Bits: 101 und 011. Nur wo BEIDE 1 sind, bleibt 1 → 001 = 1.', 'tech': 'Bitweises UND: 0b101 & 0b011 = 0b001 = 1.', 'trap': False, 'run': True, 'v': 'both', 'id': 18, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(5 | 3)', 'p': 'What is the output of the following code?', 'o': ['8', '7', '1', '2'], 'a': 1, 'kid': '| ist bitweises ODER: wo mindestens eins 1 ist → 111 = 7.', 'tech': '0b101 | 0b011 = 0b111 = 7.', 'trap': False, 'run': True, 'v': 'both', 'id': 19, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(5 ^ 3)', 'p': 'What is the output of the following code?', 'o': ['125', '6', '2', '8'], 'a': 1, 'kid': "^ ist NICHT 'hoch'! Es ist XOR: 1 nur da, wo die Bits verschieden sind → 110 = 6.", 'tech': '^ ist bitweises XOR. Potenz wäre **.', 'trap': True, 'run': True, 'v': 'both', 'id': 20, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(~5)', 'p': 'What is the output of the following code?', 'o': ['-5', '-6', '4', '5'], 'a': 1, 'kid': 'Die Schlange ~ dreht alles um. Merkformel: ~x = -x - 1. Also ~5 = -6.', 'tech': 'Bitweises NOT: ~x == -(x+1).', 'trap': True, 'run': True, 'v': 'both', 'id': 21, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(1 << 3)', 'p': 'What is the output of the following code?', 'o': ['3', '8', '4', '13'], 'a': 1, 'kid': '<< schiebt die Bits nach links, jeder Schritt = mal 2. 1 → 2 → 4 → 8.', 'tech': 'x << n == x * 2**n.', 'trap': False, 'run': True, 'v': 'both', 'id': 22, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(16 >> 2)', 'p': 'What is the output of the following code?', 'o': ['64', '4', '8', '14'], 'a': 1, 'kid': '>> schiebt nach rechts, jeder Schritt = durch 2 (ganzzahlig). 16 → 8 → 4.', 'tech': 'x >> n == x // 2**n.', 'trap': False, 'run': True, 'v': 'both', 'id': 23, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(2 + 3 * 4 ** 2)', 'p': 'What is the output of the following code?', 'o': ['400', '50', '196', '62'], 'a': 1, 'kid': 'Reihenfolge: erst **, dann *, dann +. 4**2 = 16, 3*16 = 48, 2+48 = 50.', 'tech': 'Rangfolge: ** > unäres +/- > * / // % > + -.', 'trap': False, 'run': True, 'v': 'both', 'id': 24, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(10 - 4 - 3)', 'p': 'What is the output of the following code?', 'o': ['9', '3', '-3', '17'], 'a': 1, 'kid': 'Minus wird ganz normal von links nach rechts gerechnet: (10-4) - 3 = 3.', 'tech': 'Bis auf ** sind die Operatoren linksassoziativ.', 'trap': False, 'run': True, 'v': 'both', 'id': 25, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'x = 10\nx += 5\nx //= 4\nprint(x)', 'p': 'What is the output of the following code?', 'o': ['3.75', '3', '4', '15'], 'a': 1, 'kid': 'x wird 15, dann 15 // 4 = 3 (Rest wird weggeworfen).', 'tech': 'Erweiterte Zuweisung: x //= 4 ist x = x // 4.', 'trap': False, 'run': True, 'v': 'both', 'id': 26, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print("ab" * 3)', 'p': 'What is the output of the following code?', 'o': ['ababab', 'ab3', 'Error', 'aaabbb'], 'a': 0, 'kid': 'Text mal Zahl = Text so oft hintereinander kopieren.', 'tech': 'str * int wiederholt den String.', 'trap': False, 'run': True, 'v': 'both', 'id': 27, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print("5" + "5")', 'p': 'What is the output of the following code?', 'o': ['10', '55', 'Error', '5 5'], 'a': 1, 'kid': 'Zwei Texte mit + werden aneinandergeklebt, nicht gerechnet.', 'tech': '+ auf str = Konkatenation.', 'trap': False, 'run': True, 'v': 'both', 'id': 28, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print("5" + 5)', 'p': 'What is the output of the following code?', 'o': ['10', '55', 'TypeError', 'ValueError'], 'a': 2, 'kid': 'Text + Zahl? Python weiß nicht, ob es kleben oder rechnen soll, und streikt.', 'tech': 'str + int → TypeError (falscher TYP). ValueError wäre richtiger Typ, falscher Wert.', 'trap': True, 'run': True, 'v': 'both', 'id': 29, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(3 == 3.0)', 'p': 'What is the output of the following code?', 'o': ['True', 'False', 'Error', 'None'], 'a': 0, 'kid': '== schaut nur auf den Wert. 3 und 3.0 sind gleich viel.', 'tech': 'Gleichheit vergleicht Werte über Typgrenzen int/float hinweg.', 'trap': False, 'run': True, 'v': 'both', 'id': 30, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(not 0)', 'p': 'What is the output of the following code?', 'o': ['0', 'True', 'False', '1'], 'a': 1, 'kid': "0 gilt als 'falsch'. not dreht es um → True.", 'tech': "0, 0.0, '', [], (), {} und None sind falsy.", 'trap': False, 'run': True, 'v': 'both', 'id': 31, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(1_000_000)', 'p': 'What is the output of the following code?', 'o': ['1_000_000', '1000000', '1 000 000', 'Error'], 'a': 1, 'kid': 'Die Unterstriche sind nur Deko für deine Augen. Python ignoriert sie.', 'tech': 'Unterstriche in Zahl-Literalen sind erlaubt (seit 3.6) und werden ignoriert.', 'trap': False, 'run': True, 'v': 'both', 'id': 32, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': '', 'p': 'Which of the following is NOT a valid variable name?', 'o': ['_var', 'var1', '1var', 'Var'], 'a': 2, 'kid': 'Ein Name darf nicht mit einer Ziffer anfangen. Buchstabe oder _ zuerst!', 'tech': 'Identifier: beginnt mit Buchstabe oder _, danach Buchstaben, Ziffern, _.', 'trap': False, 'run': False, 'v': 'both', 'id': 33, 'de': 'Welcher der folgenden Namen ist KEIN gültiger Variablenname in Python?'}, {'b': 1, 'code': '', 'p': 'Which of the following is a Python keyword?', 'o': ['print', 'input', 'None', 'len'], 'a': 2, 'kid': 'print, input, len sind nur Funktionen (Werkzeuge). None ist ein reserviertes Schlüsselwort.', 'tech': 'Keywords: True, False, None, if, for, def, ... Builtins wie print sind KEINE Keywords.', 'trap': True, 'run': False, 'v': 'both', 'id': 34, 'de': 'Welches der folgenden Wörter ist ein reserviertes Python-Schlüsselwort (Keyword)?'}, {'b': 1, 'code': '', 'p': 'Which statement about Python is true?', 'o': ['Python code is executed by an interpreter', 'Python must be compiled to machine code before every run by the programmer', 'Python can only run in a web browser', 'Python has no syntax rules'], 'a': 0, 'kid': 'Python hat einen Dolmetscher (Interpreter), der deinen Code Zeile für Zeile vorliest und ausführt.', 'tech': 'CPython übersetzt intern in Bytecode, aber für PCEP gilt: Python ist eine interpretierte Sprache.', 'trap': False, 'run': False, 'v': 'both', 'id': 35, 'de': 'Welche Aussage über die Programmiersprache Python ist wahr?'}, {'b': 1, 'code': '', 'p': 'A program runs without crashing but calculates the wrong result because of a logical mistake. What kind of error is it?', 'o': ['lexical', 'syntactic', 'semantic', 'no error'], 'a': 2, 'kid': 'Die Wörter sind richtig, der Satz ist grammatisch richtig – aber er ergibt keinen Sinn. Das ist ein semantischer Fehler.', 'tech': 'Lexik = erlaubte Wörter, Syntax = Grammatik, Semantik = Bedeutung.', 'trap': False, 'run': False, 'v': 'both', 'id': 36, 'de': 'Ein Programm läuft ohne Absturz durch, berechnet aber wegen eines Denkfehlers das falsche Ergebnis. Welche Art von Fehler ist das?'}, {'b': 1, 'code': 'print(0.1 + 0.2 == 0.3)', 'p': 'What is the output of the following code?', 'o': ['True', 'False', 'Error', '0.3'], 'a': 1, 'kid': 'Computer können Kommazahlen nicht ganz genau speichern. 0.1 + 0.2 ist in Wahrheit 0.30000000000000004.', 'tech': 'Floating-Point-Ungenauigkeit: niemals floats mit == vergleichen.', 'trap': True, 'run': True, 'v': 'both', 'id': 37, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(type(5 / 1))', 'p': 'What is the output of the following code?', 'o': ["<class 'int'>", "<class 'float'>", "<class 'number'>", '5.0'], 'a': 1, 'kid': 'Wieder der /-Zauberer: Ergebnis ist IMMER float.', 'tech': 'type() zeigt die Klasse: float.', 'trap': False, 'run': True, 'v': 'both', 'id': 38, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(10 % 3 ** 2)', 'p': 'What is the output of the following code?', 'o': ['1', '0', '10', '9'], 'a': 0, 'kid': 'Erst ** (3**2 = 9), dann % : 10 % 9 = 1.', 'tech': '** hat höhere Priorität als %.', 'trap': False, 'run': True, 'v': 'both', 'id': 39, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(True and False or True)', 'p': 'What is the output of the following code?', 'o': ['True', 'False', 'None', 'Error'], 'a': 0, 'kid': 'and kommt vor or. (True and False) = False. False or True = True.', 'tech': 'Priorität: not > and > or.', 'trap': False, 'run': True, 'v': 'both', 'id': 40, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(5 > 3 > 1)', 'p': 'What is the output of the following code?', 'o': ['True', 'False', 'Error', '1'], 'a': 0, 'kid': 'Python liest das wie Mathe: 5 > 3 UND 3 > 1. Beides stimmt.', 'tech': 'Verkettete Vergleiche: a > b > c ist a > b and b > c.', 'trap': False, 'run': True, 'v': 'both', 'id': 41, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': "print(3 * '7')", 'p': 'What is the output of the following code?', 'o': ['21', '777', 'Error', "'7''7''7'"], 'a': 1, 'kid': 'Zahl mal Text geht auch andersrum – der Text wird 3-mal kopiert.', 'tech': 'int * str = Wiederholung.', 'trap': False, 'run': True, 'v': 'both', 'id': 42, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(11 // 2 * 2 + 11 % 2)', 'p': 'What is the output of the following code?', 'o': ['11', '12', '10', '5'], 'a': 0, 'kid': '11//2 = 5, mal 2 = 10, plus Rest 1 = 11. Das ist die heilige Formel: (a//b)*b + a%b = a.', 'tech': 'Diese Identität gilt immer.', 'trap': False, 'run': True, 'v': 'both', 'id': 43, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'x = 5\ny = x\nx = 7\nprint(y)', 'p': 'What is the output of the following code?', 'o': ['7', '5', 'None', 'Error'], 'a': 1, 'kid': 'y hat sich die 5 gemerkt. Dass x danach ein neues Etikett kriegt, interessiert y nicht.', 'tech': 'Zahlen sind unveränderlich; x = 7 bindet x nur neu.', 'trap': False, 'run': True, 'v': 'both', 'id': 44, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'for i in range(1, 5, 2):\n    print(i, end=",")', 'p': 'What is the output of the following code?', 'o': ['1,2,3,4,', '1,3,', '1,3,5,', '2,4,'], 'a': 1, 'kid': 'range(Start, Stopp, Schritt): Start bei 1, immer +2, aber die 5 (Stopp) ist NIE dabei. → 1, 3.', 'tech': 'range schließt den Stop-Wert aus.', 'trap': True, 'run': True, 'v': 'both', 'id': 45, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'for i in range(3):\n    pass\nprint(i)', 'p': 'What is the output of the following code?', 'o': ['3', '2', '0', 'NameError'], 'a': 1, 'kid': 'range(3) ist 0, 1, 2. Nach der Schleife bleibt i auf dem letzten Wert stehen: 2.', 'tech': 'Die Schleifenvariable existiert nach der Schleife weiter.', 'trap': True, 'run': True, 'v': 'both', 'id': 46, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'print(list(range(10, 0, -3)))', 'p': 'What is the output of the following code?', 'o': ['[10, 7, 4, 1]', '[10, 7, 4, 1, -2]', '[10, 7, 4]', '[]'], 'a': 0, 'kid': 'Rückwärts in 3er-Schritten: 10, 7, 4, 1. Die 0 ist Stopp, also nicht dabei (und -2 wäre schon drüber).', 'tech': 'Negativer step zählt abwärts; stop wird ausgeschlossen.', 'trap': False, 'run': True, 'v': 'both', 'id': 47, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'c = 0\nfor i in range(5, 1):\n    c += 1\nprint(c)', 'p': 'What is the output of the following code?', 'o': ['4', '0', '5', 'Error'], 'a': 1, 'kid': 'Von 5 bis 1 VORWÄRTS zählen geht nicht. Die Schleife läuft kein einziges Mal.', 'tech': 'range(5, 1) ist leer, weil step standardmäßig +1 ist.', 'trap': True, 'run': True, 'v': 'both', 'id': 48, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'for i in range(5):\n    if i == 2:\n        continue\n    if i == 4:\n        break\n    print(i, end="")', 'p': 'What is the output of the following code?', 'o': ['0123', '013', '01', '0134'], 'a': 1, 'kid': "continue = 'diese Runde überspringen' (2 fehlt). break = 'Schleife sofort beenden' (bei 4 Schluss).", 'tech': 'Ausgabe für i=0,1,3. Bei i=4 break vor dem print.', 'trap': False, 'run': True, 'v': 'both', 'id': 49, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'for i in range(3):\n    pass\nelse:\n    print("done")', 'p': 'What is the output of the following code?', 'o': ['done', 'nothing', 'done done done', 'SyntaxError'], 'a': 0, 'kid': "Das else unter einer Schleife heißt: 'Wenn du OHNE break fertig geworden bist, mach das hier.'", 'tech': 'Loop-else läuft, wenn die Schleife normal endet (kein break).', 'trap': True, 'run': True, 'v': 'both', 'id': 50, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'for i in range(3):\n    if i == 1:\n        break\nelse:\n    print("A")\nprint("B")', 'p': 'What is the output of the following code?', 'o': ['A\nB', 'B', 'A', 'nothing'], 'a': 1, 'kid': 'Es gab ein break → das Schleifen-else wird übersprungen. Nur B kommt.', 'tech': 'break unterdrückt den else-Zweig der Schleife.', 'trap': True, 'run': True, 'v': 'both', 'id': 51, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'i = 0\nwhile i < 3:\n    i += 1\nelse:\n    print(i)', 'p': 'What is the output of the following code?', 'o': ['2', '3', '0', 'nothing'], 'a': 1, 'kid': 'while kann auch ein else haben! Die Schleife endet normal mit i = 3, dann läuft das else.', 'tech': 'while-else: else läuft, wenn die Bedingung False wird (kein break).', 'trap': True, 'run': True, 'v': 'both', 'id': 52, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'i = 10\nc = 0\nwhile i > 0:\n    i -= 3\n    c += 1\nprint(c)', 'p': 'What is the output of the following code?', 'o': ['3', '4', '5', '10'], 'a': 1, 'kid': 'i: 10 → 7 → 4 → 1 → -2. Das sind 4 Runden.', 'tech': 'Schleifen-Tracing: Zähle jede Ausführung des Körpers.', 'trap': False, 'run': True, 'v': 'both', 'id': 53, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'x = 5\nif x > 3:\n    print("A")\nelif x > 4:\n    print("B")\nelse:\n    print("C")', 'p': 'What is the output of the following code?', 'o': ['A', 'B', 'A\nB', 'C'], 'a': 0, 'kid': 'Bei if/elif gewinnt der ERSTE Treffer. Danach wird der Rest ignoriert, auch wenn er auch stimmen würde.', 'tech': 'Nur ein Zweig einer if-elif-else-Kette wird ausgeführt.', 'trap': True, 'run': True, 'v': 'both', 'id': 54, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'x = 0\nif x:\n    print("yes")\nelse:\n    print("no")', 'p': 'What is the output of the following code?', 'o': ['yes', 'no', '0', 'Error'], 'a': 1, 'kid': "0 gilt als 'falsch', also geht's in den else-Zweig.", 'tech': 'Truthiness: 0 ist falsy.', 'trap': False, 'run': True, 'v': 'both', 'id': 55, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'c = 0\nfor i in range(3):\n    for j in range(i):\n        c += 1\nprint(c)', 'p': 'What is the output of the following code?', 'o': ['9', '3', '6', '0'], 'a': 1, 'kid': 'i=0: innen 0 Runden, i=1: 1 Runde, i=2: 2 Runden. 0+1+2 = 3.', 'tech': 'Innere Schleife hängt von i ab: range(0), range(1), range(2).', 'trap': False, 'run': True, 'v': 'both', 'id': 56, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'for ch in "abc":\n    print(ch * 2, end="")', 'p': 'What is the output of the following code?', 'o': ['abcabc', 'aabbcc', 'a2b2c2', 'Error'], 'a': 1, 'kid': 'for geht Buchstabe für Buchstabe durch den Text, jeder wird verdoppelt.', 'tech': 'Strings sind iterierbar.', 'trap': False, 'run': True, 'v': 'both', 'id': 57, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'i = 0\nwhile True:\n    i += 1\n    if i == 3:\n        break\nprint(i)', 'p': 'What is the output of the following code?', 'o': ['2', '3', '4', 'infinite loop'], 'a': 1, 'kid': 'while True läuft ewig – außer jemand ruft break. Bei i == 3 ist Schluss.', 'tech': 'while True + break ist ein übliches Muster.', 'trap': False, 'run': True, 'v': 'both', 'id': 58, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'i = 0\nwhile i < 5:\n    print(i)', 'p': 'What happens when this code runs?', 'o': ['0 to 4 is printed', 'nothing is printed', 'the loop runs forever', 'SyntaxError'], 'a': 2, 'kid': 'i wird nie größer! 0 ist immer kleiner als 5 → die Schleife hört nie auf.', 'tech': 'Endlosschleife, weil die Bedingungsvariable nicht verändert wird.', 'trap': True, 'run': False, 'v': 'both', 'id': 59, 'de': 'Was passiert, wenn dieser Code ausgeführt wird?'}, {'b': 2, 'code': 'for i in range(1, 10, 3):\n    pass\nprint(i)', 'p': 'What is the output of the following code?', 'o': ['10', '9', '7', '3'], 'a': 2, 'kid': 'range(1, 10, 3) = 1, 4, 7. Die 10 ist nie dabei. Letzter Wert: 7.', 'tech': 'Letzter Wert von range(start, stop, step).', 'trap': False, 'run': True, 'v': 'both', 'id': 60, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'i = 0\ns = 0\nwhile i < 5:\n    i += 1\n    if i % 2 == 0:\n        continue\n    s += i\nprint(s)', 'p': 'What is the output of the following code?', 'o': ['15', '9', '6', '4'], 'a': 1, 'kid': 'Gerade Zahlen werden übersprungen (continue). Addiert werden nur 1 + 3 + 5 = 9.', 'tech': 'continue springt zurück zur Bedingung.', 'trap': False, 'run': True, 'v': 'both', 'id': 61, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': '', 'p': 'What does the pass statement do?', 'o': ['It ends the loop', 'It skips to the next iteration', 'It does nothing; it is a placeholder', 'It raises an error'], 'a': 2, 'kid': "pass ist das Nichtstun-Wort. Wie ein Schild 'hier kommt später was'.", 'tech': 'pass ist eine leere Anweisung, z. B. für leere Blöcke.', 'trap': False, 'run': False, 'v': 'both', 'id': 62, 'de': "Was bewirkt die Anweisung 'pass' in Python?"}, {'b': 2, 'code': 'x = 10\nif x > 5:\n    if x > 8:\n        print("big")\n    else:\n        print("medium")', 'p': 'What is the output of the following code?', 'o': ['big', 'medium', 'big\nmedium', 'nothing'], 'a': 0, 'kid': 'Erst die äußere Tür (x > 5, ja), dann die innere Tür (x > 8, ja) → big.', 'tech': 'Verschachtelte Bedingungen von außen nach innen lesen; else gehört zum inneren if (Einrückung!).', 'trap': False, 'run': True, 'v': 'both', 'id': 63, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'for i in range(2):\n    for j in range(2):\n        if j == 1:\n            break\n        print(i, j)', 'p': 'What is the output of the following code?', 'o': ['0 0\n1 0', '0 0\n0 1\n1 0\n1 1', '0 0', '0 0\n0 1'], 'a': 0, 'kid': 'break bricht nur die INNERE Schleife ab. Die äußere läuft brav weiter.', 'tech': 'break wirkt nur auf die innerste Schleife.', 'trap': True, 'run': True, 'v': 'both', 'id': 64, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'x = 3\nwhile x:\n    x -= 1\n    print(x, end="")', 'p': 'What is the output of the following code?', 'o': ['321', '210', '3210', '21'], 'a': 1, 'kid': "Erst wird x kleiner, DANN gedruckt: 2, 1, 0. Bei x = 0 ist 'while x' falsch → Schluss.", 'tech': 'while x ist gleich while x != 0.', 'trap': False, 'run': True, 'v': 'both', 'id': 65, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'if "":\n    print("A")\nelif []:\n    print("B")\nelse:\n    print("C")', 'p': 'What is the output of the following code?', 'o': ['A', 'B', 'C', 'Error'], 'a': 2, 'kid': "Leerer Text und leere Liste sind beide 'falsch'. Also bleibt nur else.", 'tech': 'Leere Container sind falsy.', 'trap': False, 'run': True, 'v': 'both', 'id': 66, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'n = 0\nfor i in range(2, 8, 2):\n    n += i\nprint(n)', 'p': 'What is the output of the following code?', 'o': ['20', '12', '8', '14'], 'a': 1, 'kid': '2 + 4 + 6 = 12. Die 8 ist Stopp und nicht dabei.', 'tech': 'range(2, 8, 2) → 2, 4, 6.', 'trap': False, 'run': True, 'v': 'both', 'id': 67, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'for i in range(3):\n    print("*" * i)', 'p': 'What is the output of the following code?', 'o': ['\n*\n**', '*\n**\n***', '***', '*\n**'], 'a': 0, 'kid': "i ist 0, 1, 2. '*' mal 0 = leere Zeile! Dann * und **.", 'tech': "Die erste Zeile ist leer, weil '*' * 0 == ''.", 'trap': True, 'run': True, 'v': 'both', 'id': 68, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'x = 1\nwhile x < 100:\n    x *= 3\nprint(x)', 'p': 'What is the output of the following code?', 'o': ['81', '243', '99', '100'], 'a': 1, 'kid': '1 → 3 → 9 → 27 → 81 → 243. Bei 81 ist die Bedingung noch wahr, also noch einmal mal 3.', 'tech': 'Die Bedingung wird VOR jeder Runde geprüft.', 'trap': False, 'run': True, 'v': 'both', 'id': 69, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'for i in range(4):\n    if i % 2:\n        print(i, end="")\n    else:\n        continue', 'p': 'What is the output of the following code?', 'o': ['13', '02', '0123', 'nothing'], 'a': 0, 'kid': 'i % 2 ist 1 (wahr) bei ungeraden Zahlen → 1 und 3 werden gedruckt.', 'tech': 'Ungerade: i % 2 == 1 → truthy.', 'trap': False, 'run': True, 'v': 'both', 'id': 70, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'x = 7\nif x % 2 == 0:\n    print("even")\nelif x % 3 == 0:\n    print("three")\nprint("end")', 'p': 'What is the output of the following code?', 'o': ['odd\nend', 'end', 'three\nend', 'even\nend'], 'a': 1, 'kid': "7 ist nicht gerade, nicht durch 3 teilbar, und es gibt kein else. Also nur 'end'.", 'tech': 'Ohne else wird bei keinem Treffer nichts aus der Kette ausgeführt.', 'trap': False, 'run': True, 'v': 'both', 'id': 71, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 2, 'code': 'for i in range(0, 10, 4):\n    print(i, end=" ")\nprint(len(range(0, 10, 4)))', 'p': 'What is the output of the following code?', 'o': ['0 4 8 3', '0 4 8 2', '0 4 8 12 4', '0 4 3'], 'a': 0, 'kid': '0, 4, 8 – die 12 wäre schon über 10. Drei Zahlen, also len = 3.', 'tech': 'len(range(...)) zählt die Werte.', 'trap': False, 'run': True, 'v': 'both', 'id': 72, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3, 4, 5]\nprint(l[1:4])', 'p': 'What is the output of the following code?', 'o': ['[1, 2, 3, 4]', '[2, 3, 4]', '[2, 3, 4, 5]', '[1, 2, 3]'], 'a': 1, 'kid': 'Index fängt bei 0 an! l[1] ist die 2. Und das Ende (Index 4) ist NICHT dabei.', 'tech': 'Slice [start:stop] – stop exklusiv.', 'trap': True, 'run': True, 'v': 'both', 'id': 73, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3, 4, 5]\nprint(l[::-1])', 'p': 'What is the output of the following code?', 'o': ['[1, 2, 3, 4, 5]', '[5, 4, 3, 2, 1]', '[5]', 'Error'], 'a': 1, 'kid': 'Schritt -1 heißt: rückwärts laufen. Die Liste wird umgedreht.', 'tech': '[::-1] ist der Standard-Trick zum Umkehren.', 'trap': False, 'run': True, 'v': 'both', 'id': 74, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3, 4, 5]\nprint(l[-2])', 'p': 'What is the output of the following code?', 'o': ['2', '4', '-2', 'Error'], 'a': 1, 'kid': 'Negative Zahlen zählen von hinten: -1 ist die Letzte, -2 die Vorletzte.', 'tech': 'l[-n] == l[len(l)-n].', 'trap': False, 'run': True, 'v': 'both', 'id': 75, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3, 4, 5]\nprint(l[::2])', 'p': 'What is the output of the following code?', 'o': ['[1, 3, 5]', '[2, 4]', '[1, 2]', '[1, 3]'], 'a': 0, 'kid': 'Von Anfang bis Ende, aber jeden zweiten nehmen: 1, 3, 5.', 'tech': 'Step 2 nimmt jedes zweite Element.', 'trap': False, 'run': True, 'v': 'both', 'id': 76, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3, 4, 5]\nprint(l[1:10])', 'p': 'What is the output of the following code?', 'o': ['IndexError', '[2, 3, 4, 5]', '[1, 2, 3, 4, 5]', '[]'], 'a': 1, 'kid': 'Beim Slicen ist Python nett: zu große Grenzen werden einfach abgeschnitten. Kein Fehler!', 'tech': 'Slices werfen keinen IndexError, nur Einzelzugriffe wie l[10].', 'trap': True, 'run': True, 'v': 'both', 'id': 77, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3]\nprint(l[3])', 'p': 'What is the output of the following code?', 'o': ['3', 'None', 'IndexError', '[]'], 'a': 2, 'kid': "Die Liste hat Plätze 0, 1, 2. Platz 3 gibt's nicht → Fehler.", 'tech': 'Einzelzugriff außerhalb → IndexError.', 'trap': False, 'run': True, 'v': 'both', 'id': 78, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'a = [1, 2, 3]\nb = a\nb.append(4)\nprint(a)', 'p': 'What is the output of the following code?', 'o': ['[1, 2, 3]', '[1, 2, 3, 4]', '[4]', 'Error'], 'a': 1, 'kid': 'b = a macht KEINE Kopie. Es klebt nur ein zweites Namensschild auf DIESELBE Kiste. Änderst du b, änderst du a.', 'tech': 'Zuweisung kopiert die Referenz, nicht die Liste. Kopie: a[:] oder list(a).', 'trap': True, 'run': True, 'v': 'both', 'id': 79, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'a = [1, 2, 3]\nb = a[:]\nb.append(4)\nprint(a)', 'p': 'What is the output of the following code?', 'o': ['[1, 2, 3]', '[1, 2, 3, 4]', '[4]', 'Error'], 'a': 0, 'kid': 'a[:] baut eine NEUE Kiste mit denselben Sachen. Jetzt sind es zwei getrennte Listen.', 'tech': 'Slicing [:] erzeugt eine (flache) Kopie.', 'trap': False, 'run': True, 'v': 'both', 'id': 80, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 't = (5)\nprint(type(t))', 'p': 'What is the output of the following code?', 'o': ["<class 'tuple'>", "<class 'int'>", "<class 'list'>", 'Error'], 'a': 1, 'kid': 'Klammern allein machen kein Tupel – das ist nur Mathe-Klammer. Das Komma macht das Tupel: (5,).', 'tech': 'Ein-Element-Tupel braucht ein Komma: (5,).', 'trap': True, 'run': True, 'v': 'both', 'id': 81, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 't = (1, 2, 3)\nt[0] = 9\nprint(t)', 'p': 'What is the output of the following code?', 'o': ['(9, 2, 3)', '(1, 2, 3)', 'TypeError', 'IndexError'], 'a': 2, 'kid': 'Tupel sind wie ein versiegeltes Glas: anschauen ja, ändern nein.', 'tech': 'Tupel sind immutable → TypeError bei Zuweisung.', 'trap': True, 'run': True, 'v': 'both', 'id': 82, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3]\nl.insert(1, 9)\nprint(l)', 'p': 'What is the output of the following code?', 'o': ['[9, 1, 2, 3]', '[1, 9, 2, 3]', '[1, 2, 9, 3]', '[1, 9, 3]'], 'a': 1, 'kid': 'insert(Platz, Ding): Die 9 drängelt sich auf Platz 1, alle anderen rücken nach hinten.', 'tech': 'insert(index, value) schiebt ein, ersetzt nichts.', 'trap': False, 'run': True, 'v': 'both', 'id': 83, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3]\ndel l[0]\nprint(l)', 'p': 'What is the output of the following code?', 'o': ['[2, 3]', '[1, 2]', '[0, 2, 3]', '[1, 2, 3]'], 'a': 0, 'kid': 'del l[0] wirft das Ding auf Platz 0 raus.', 'tech': 'del entfernt per Index.', 'trap': False, 'run': True, 'v': 'both', 'id': 84, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'd = {"a": 1, "b": 2}\nprint(d["c"])', 'p': 'What is the output of the following code?', 'o': ['None', '0', 'KeyError', 'IndexError'], 'a': 2, 'kid': "Den Schlüssel 'c' gibt's nicht im Wörterbuch. Mit [] gibt's dann einen Fehler.", 'tech': 'Fehlender Key bei d[key] → KeyError (nicht IndexError!).', 'trap': True, 'run': True, 'v': 'both', 'id': 85, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'd = {"a": 1, "b": 2}\nprint(d.get("c"))', 'p': 'What is the output of the following code?', 'o': ['None', '0', 'KeyError', 'c'], 'a': 0, 'kid': '.get() ist die höfliche Version: Wenn nichts da ist, sagt sie leise None statt zu schreien.', 'tech': 'd.get(key) → None, d.get(key, default) → default.', 'trap': False, 'run': True, 'v': 'both', 'id': 86, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'd = {"a": 1}\nd["a"] = 5\nd["b"] = 2\nprint(len(d))', 'p': 'What is the output of the following code?', 'o': ['3', '2', '1', 'Error'], 'a': 1, 'kid': "'a' wird nur überschrieben (keine neue Schublade). 'b' kommt neu dazu. Also 2 Schubladen.", 'tech': 'Keys sind eindeutig; Zuweisung auf bestehenden Key aktualisiert.', 'trap': False, 'run': True, 'v': 'both', 'id': 87, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'for k, v in {"x": 1, "y": 2}.items():\n    print(k + str(v), end="")', 'p': 'What is the output of the following code?', 'o': ['x1y2', 'xy12', '(x,1)(y,2)', 'Error'], 'a': 0, 'kid': '.items() gibt immer Paare (Schlüssel, Wert). Die packen wir in k und v aus.', 'tech': 'items() liefert (key, value)-Tupel.', 'trap': False, 'run': True, 'v': 'both', 'id': 88, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print(list({"a": 1, "b": 2}.keys()))', 'p': 'What is the output of the following code?', 'o': ["['a', 'b']", '[1, 2]', "[('a', 1), ('b', 2)]", 'a b'], 'a': 0, 'kid': '.keys() = nur die Namen der Schubladen.', 'tech': 'keys() → Schlüssel, values() → Werte, items() → Paare.', 'trap': False, 'run': True, 'v': 'both', 'id': 89, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 's = "Python"\nprint(s[1:3])', 'p': 'What is the output of the following code?', 'o': ['Py', 'yt', 'yth', 'Pyt'], 'a': 1, 'kid': "P=0, y=1, t=2, h=3. Von 1 bis vor 3 → 'yt'.", 'tech': 'Strings slicen wie Listen.', 'trap': False, 'run': True, 'v': 'both', 'id': 90, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 's = "hello"\ns[0] = "H"\nprint(s)', 'p': 'What is the output of the following code?', 'o': ['Hello', 'hello', 'TypeError', 'ValueError'], 'a': 2, 'kid': 'Strings sind wie Tupel: in Stein gemeißelt. Einzelne Buchstaben kannst du nicht austauschen.', 'tech': 'str ist immutable → TypeError.', 'trap': True, 'run': True, 'v': 'both', 'id': 91, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 's = "abc"\ns.upper()\nprint(s)', 'p': 'What is the output of the following code?', 'o': ['ABC', 'abc', 'None', 'Error'], 'a': 1, 'kid': 'upper() gibt dir eine NEUE großgeschriebene Kopie. Aber du hast sie nicht aufgefangen! s bleibt klein.', 'tech': 'String-Methoden ändern nie das Original. Richtig: s = s.upper().', 'trap': True, 'run': True, 'v': 'both', 'id': 92, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print(len("Hi\\n"))', 'p': 'What is the output of the following code?', 'o': ['4', '3', '2', 'Error'], 'a': 1, 'kid': '\\n sieht aus wie 2 Zeichen, ist aber EIN Zeichen (der Zeilenumbruch).', 'tech': 'Escape-Sequenzen zählen als ein Zeichen.', 'trap': True, 'run': True, 'v': 'both', 'id': 93, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print("a,b,c".split(","))', 'p': 'What is the output of the following code?', 'o': ["['a', 'b', 'c']", "['a,b,c']", "('a', 'b', 'c')", 'abc'], 'a': 0, 'kid': 'split zerschneidet den Text an jedem Komma und gibt eine Liste.', 'tech': 'split(sep) → Liste von Strings.', 'trap': False, 'run': True, 'v': 'both', 'id': 94, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print("-".join(["a", "b"]))', 'p': 'What is the output of the following code?', 'o': ['a-b', '-a-b-', "['a', 'b']", 'a b'], 'a': 0, 'kid': "join ist das Gegenteil von split: Es klebt die Teile mit '-' zusammen.", 'tech': 'sep.join(liste) – nur zwischen die Elemente.', 'trap': False, 'run': True, 'v': 'both', 'id': 95, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [3, 1, 2]\nprint(l.sort())', 'p': 'What is the output of the following code?', 'o': ['[1, 2, 3]', 'None', '[3, 1, 2]', 'Error'], 'a': 1, 'kid': '.sort() sortiert die Liste heimlich an Ort und Stelle und gibt NICHTS (None) zurück.', 'tech': 'list.sort() → None. sorted(l) gibt eine neue Liste zurück.', 'trap': True, 'run': True, 'v': 'both', 'id': 96, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [3, 1, 2]\nprint(sorted(l), l)', 'p': 'What is the output of the following code?', 'o': ['[1, 2, 3] [1, 2, 3]', '[1, 2, 3] [3, 1, 2]', 'None [1, 2, 3]', '[3, 1, 2] [3, 1, 2]'], 'a': 1, 'kid': 'sorted() macht eine neue, sortierte Kopie. Das Original bleibt unordentlich.', 'tech': 'sorted() ist nicht in-place.', 'trap': False, 'run': True, 'v': 'both', 'id': 97, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'm = [[1, 2], [3, 4]]\nprint(m[1][0])', 'p': 'What is the output of the following code?', 'o': ['2', '3', '1', '4'], 'a': 1, 'kid': 'm[1] ist die zweite innere Liste [3, 4]. Davon Platz 0 → 3.', 'tech': 'Mehrdimensionale Listen: erst Zeile, dann Spalte.', 'trap': False, 'run': True, 'v': 'both', 'id': 98, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print([1, 2] + [3])', 'p': 'What is the output of the following code?', 'o': ['[1, 2, 3]', '[1, 2, [3]]', '[4, 5]', 'Error'], 'a': 0, 'kid': '+ klebt zwei Listen zu einer zusammen.', 'tech': 'Listen-Konkatenation.', 'trap': False, 'run': True, 'v': 'both', 'id': 99, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print([0] * 3)', 'p': 'What is the output of the following code?', 'o': ['[0, 0, 0]', '[0]', '0', '[[0], [0], [0]]'], 'a': 0, 'kid': 'Liste mal 3 = den Inhalt 3-mal reinkopieren.', 'tech': 'list * int wiederholt die Elemente.', 'trap': False, 'run': True, 'v': 'both', 'id': 100, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print(3 in [1, 2, 3])', 'p': 'What is the output of the following code?', 'o': ['True', 'False', '2', 'Error'], 'a': 0, 'kid': 'in fragt: Ist das Ding in der Kiste? Ja!', 'tech': 'Membership-Operator.', 'trap': False, 'run': True, 'v': 'both', 'id': 101, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3]\nl.append([4, 5])\nprint(len(l))', 'p': 'What is the output of the following code?', 'o': ['5', '4', '3', 'Error'], 'a': 1, 'kid': 'append packt das GANZE Ding als EIN Element rein – hier eine ganze Liste als ein Päckchen.', 'tech': 'append fügt genau ein Element hinzu (auch wenn es eine Liste ist).', 'trap': True, 'run': True, 'v': 'both', 'id': 102, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3, 4]\nprint(l.pop(), l)', 'p': 'What is the output of the following code?', 'o': ['4 [1, 2, 3]', '1 [2, 3, 4]', '4 [1, 2, 3, 4]', 'None [1, 2, 3]'], 'a': 0, 'kid': 'pop() ohne Zahl nimmt das LETZTE raus und gibt es dir in die Hand.', 'tech': 'pop() entfernt und liefert das letzte Element.', 'trap': False, 'run': True, 'v': 'both', 'id': 103, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print(1 in {"a": 1})', 'p': 'What is the output of the following code?', 'o': ['True', 'False', 'KeyError', '1'], 'a': 1, 'kid': 'in schaut bei einem Wörterbuch nur auf die SCHLÜSSEL, nicht auf die Werte. 1 ist kein Schlüssel.', 'tech': 'x in dict prüft Keys. Werte: x in d.values().', 'trap': True, 'run': True, 'v': 'both', 'id': 104, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 't = (1, 2) + (3,)\nprint(t)', 'p': 'What is the output of the following code?', 'o': ['(1, 2, 3)', '(1, 2, (3,))', 'TypeError', '(4, 5)'], 'a': 0, 'kid': 'Tupel kann man nicht ändern, aber man kann zwei zu einem NEUEN zusammenkleben.', 'tech': 'Konkatenation erzeugt ein neues Tupel.', 'trap': False, 'run': True, 'v': 'both', 'id': 105, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print("Python"[-1])', 'p': 'What is the output of the following code?', 'o': ['P', 'n', 'o', 'Error'], 'a': 1, 'kid': '-1 ist immer der letzte Buchstabe.', 'tech': 'Negative Indizes auf Strings.', 'trap': False, 'run': True, 'v': 'both', 'id': 106, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3]\nfor x in l:\n    x *= 2\nprint(l)', 'p': 'What is the output of the following code?', 'o': ['[2, 4, 6]', '[1, 2, 3]', 'None', 'Error'], 'a': 1, 'kid': 'x ist nur eine Kopie des Zettels. Wenn du x verdoppelst, merkt die Liste davon nichts.', 'tech': 'Die Schleifenvariable bindet nur neu; um die Liste zu ändern: l[i] = ...', 'trap': True, 'run': True, 'v': 'both', 'id': 107, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print(list("abc"))', 'p': 'What is the output of the following code?', 'o': ["['abc']", "['a', 'b', 'c']", '[a, b, c]', 'Error'], 'a': 1, 'kid': 'list() nimmt den Text auseinander, Buchstabe für Buchstabe.', 'tech': 'list(iterable).', 'trap': False, 'run': True, 'v': 'both', 'id': 108, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [1, 2, 3]\nl[1:2] = [7, 8]\nprint(l)', 'p': 'What is the output of the following code?', 'o': ['[1, 7, 8, 3]', '[1, [7, 8], 3]', '[1, 7, 3]', 'Error'], 'a': 0, 'kid': 'Der Bereich [1:2] (nur die 2) wird durch zwei neue Sachen ersetzt. Die Liste wird länger.', 'tech': 'Slice-Zuweisung kann die Länge ändern.', 'trap': False, 'run': True, 'v': 'both', 'id': 109, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print("abcabc".find("c"))', 'p': 'What is the output of the following code?', 'o': ['2', '3', '5', '[2, 5]'], 'a': 0, 'kid': 'find sucht das ERSTE Vorkommen und sagt dir den Platz: a=0, b=1, c=2.', 'tech': 'find() → erster Index oder -1, wenn nicht gefunden.', 'trap': False, 'run': True, 'v': 'both', 'id': 110, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print("abc".find("z"))', 'p': 'What is the output of the following code?', 'o': ['None', '-1', 'ValueError', '0'], 'a': 1, 'kid': 'find ist lieb: Wenn es nichts findet, sagt es -1 statt Fehler.', 'tech': 'find() → -1; index() würde ValueError werfen.', 'trap': True, 'run': True, 'v': 'both', 'id': 111, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'd = {"a": 1, "b": 2}\ndel d["a"]\nprint(d)', 'p': 'What is the output of the following code?', 'o': ["{'b': 2}", "{'a': 1}", '{}', 'KeyError'], 'a': 0, 'kid': "del wirft die Schublade 'a' samt Inhalt raus.", 'tech': 'del d[key] entfernt einen Eintrag.', 'trap': False, 'run': True, 'v': 'both', 'id': 112, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 't = ()\nprint(len(t), type(t))', 'p': 'What is the output of the following code?', 'o': ["0 <class 'tuple'>", "1 <class 'tuple'>", "0 <class 'list'>", 'Error'], 'a': 0, 'kid': "Leere Klammern () sind ein leeres Tupel. Bei leer braucht's kein Komma.", 'tech': '() ist das leere Tupel.', 'trap': False, 'run': True, 'v': 'both', 'id': 113, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'a, b = 1, 2\na, b = b, a\nprint(a, b)', 'p': 'What is the output of the following code?', 'o': ['1 2', '2 1', '2 2', 'Error'], 'a': 1, 'kid': 'Python kann zwei Sachen in einem Schritt tauschen – ganz ohne Hilfsvariable.', 'tech': 'Tuple-Unpacking: rechts wird zuerst ausgewertet.', 'trap': False, 'run': True, 'v': 'both', 'id': 114, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 's = "Hello"\nprint(s[10:])', 'p': 'What is the output of the following code?', 'o': ['IndexError', 'an empty line', 'o', 'Hello'], 'a': 1, 'kid': 'Slice außerhalb gibt einfach einen leeren Text, keinen Fehler. print zeigt dann eine leere Zeile.', 'tech': "Slices sind tolerant: ergibt ''.", 'trap': True, 'run': False, 'v': 'both', 'id': 115, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'l = [10, 20, 30]\nprint(l.index(20))', 'p': 'What is the output of the following code?', 'o': ['20', '1', '2', 'True'], 'a': 1, 'kid': 'index() sagt dir, auf welchem PLATZ das Ding liegt.', 'tech': 'list.index(value) → Position.', 'trap': False, 'run': True, 'v': 'both', 'id': 116, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'x = [1, 2, 3]\ny = [1, 2, 3]\nprint(x == y, x is y)', 'p': 'What is the output of the following code?', 'o': ['True True', 'True False', 'False False', 'False True'], 'a': 1, 'kid': "== fragt: Sieht gleich aus? Ja. 'is' fragt: Ist es DIESELBE Kiste? Nein, zwei verschiedene Kisten.", 'tech': '== vergleicht Werte, is vergleicht Identität.', 'trap': True, 'run': True, 'v': 'both', 'id': 117, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print("hello world".title())', 'p': 'What is the output of the following code?', 'o': ['Hello world', 'Hello World', 'HELLO WORLD', 'hello World'], 'a': 1, 'kid': 'title() macht aus jedem Wort eine Überschrift: erster Buchstabe groß.', 'tech': 'capitalize() nur den ersten Buchstaben des Strings, title() jedes Wort.', 'trap': False, 'run': True, 'v': 'both', 'id': 118, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print("  hi  ".strip() + "!")', 'p': 'What is the output of the following code?', 'o': ['  hi  !', 'hi!', 'hi  !', '  hi!'], 'a': 1, 'kid': 'strip() ist der Staubsauger: Er saugt Leerzeichen links und rechts weg.', 'tech': 'strip/lstrip/rstrip entfernen Whitespace.', 'trap': False, 'run': True, 'v': 'both', 'id': 119, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 3, 'code': 'print("a\\tb" == "a b")', 'p': 'What is the output of the following code?', 'o': ['True', 'False', 'Error', 'a\\tb'], 'a': 1, 'kid': '\\t ist ein Tab, kein normales Leerzeichen. Also nicht gleich.', 'tech': '\\t ist ein eigenes Zeichen (Tabulator).', 'trap': False, 'run': True, 'v': 'both', 'id': 120, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f():\n    print("hi")\n\nx = f()\nprint(x)', 'p': 'What is the output of the following code?', 'o': ['hi\nhi', 'hi\nNone', 'None', 'Error'], 'a': 1, 'kid': "f druckt 'hi', gibt aber nichts zurück. Wenn kein return da ist, kommt automatisch None raus.", 'tech': 'Ohne return liefert jede Funktion None.', 'trap': True, 'run': True, 'v': 'both', 'id': 121, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f(a, b=2):\n    return a * b\n\nprint(f(3))', 'p': 'What is the output of the following code?', 'o': ['3', '6', 'Error', 'None'], 'a': 1, 'kid': 'b hat einen Standardwert 2. Wenn du b nicht mitgibst, nimmt er die 2.', 'tech': 'Default-Parameter.', 'trap': False, 'run': True, 'v': 'both', 'id': 122, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f(a, b):\n    return a - b\n\nprint(f(b=1, a=5))', 'p': 'What is the output of the following code?', 'o': ['-4', '4', 'Error', 'None'], 'a': 1, 'kid': 'Mit Namen (Keyword) ist die Reihenfolge egal: a ist 5, b ist 1.', 'tech': 'Keyword-Argumente werden per Name zugeordnet.', 'trap': False, 'run': True, 'v': 'both', 'id': 123, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f(a=1, b):\n    return a + b', 'p': 'What happens when this code is run?', 'o': ['it works', 'SyntaxError', 'TypeError', 'NameError'], 'a': 1, 'kid': 'Parameter mit Standardwert müssen HINTEN stehen. Sonst weiß Python nicht, wohin mit den Zahlen.', 'tech': 'Non-default argument follows default argument → SyntaxError.', 'trap': True, 'run': True, 'v': 'both', 'id': 124, 'de': 'Was passiert, wenn dieser Code ausgeführt wird?'}, {'b': 4, 'code': 'def f(a, b):\n    return a + b\n\nprint(f(a=1, 2))', 'p': 'What is the output of the following code?', 'o': ['3', 'SyntaxError', 'TypeError', '1'], 'a': 1, 'kid': 'Erst die Zahlen ohne Namen, dann die mit Namen. Andersrum ist verboten.', 'tech': 'Positional argument follows keyword argument → SyntaxError.', 'trap': True, 'run': True, 'v': 'both', 'id': 125, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f(a, b):\n    return a + b\n\nprint(f(1, 2, 3))', 'p': 'What is the output of the following code?', 'o': ['6', '3', 'TypeError', 'SyntaxError'], 'a': 2, 'kid': 'Die Funktion hat 2 Plätze, du gibst ihr 3 Sachen. Passt nicht → TypeError.', 'tech': 'Falsche Anzahl Argumente → TypeError (zur Laufzeit).', 'trap': False, 'run': True, 'v': 'both', 'id': 126, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'x = 1\ndef f():\n    x = 2\nf()\nprint(x)', 'p': 'What is the output of the following code?', 'o': ['1', '2', 'None', 'Error'], 'a': 0, 'kid': 'Das x in der Funktion ist ein eigenes, privates x. Das äußere x merkt nichts.', 'tech': 'Zuweisung in einer Funktion erzeugt eine lokale Variable.', 'trap': True, 'run': True, 'v': 'both', 'id': 127, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'x = 1\ndef f():\n    global x\n    x = 2\nf()\nprint(x)', 'p': 'What is the output of the following code?', 'o': ['1', '2', 'None', 'Error'], 'a': 1, 'kid': "global x sagt: 'Ich meine das x von draußen!' Dann wird das äußere geändert.", 'tech': 'global bindet den Namen an den Modul-Scope.', 'trap': False, 'run': True, 'v': 'both', 'id': 128, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'x = 1\ndef f():\n    print(x)\n    x = 2\nf()', 'p': 'What is the output of the following code?', 'o': ['1', '2', 'UnboundLocalError', 'None'], 'a': 2, 'kid': "Weil weiter unten x = 2 steht, hält Python x für lokal – in der GANZEN Funktion. Beim print gibt's das lokale x aber noch nicht.", 'tech': 'UnboundLocalError (Unterklasse von NameError).', 'trap': True, 'run': True, 'v': 'both', 'id': 129, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'x = 1\ndef f():\n    print(x)\nf()', 'p': 'What is the output of the following code?', 'o': ['1', 'None', 'NameError', 'UnboundLocalError'], 'a': 0, 'kid': 'Nur LESEN geht immer: Die Funktion schaut einfach nach draußen und findet x = 1.', 'tech': 'Lesender Zugriff auf globale Variable braucht kein global.', 'trap': False, 'run': True, 'v': 'both', 'id': 130, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f(n):\n    if n <= 1:\n        return 1\n    return n * f(n - 1)\n\nprint(f(4))', 'p': 'What is the output of the following code?', 'o': ['4', '10', '24', 'RecursionError'], 'a': 2, 'kid': 'Die Funktion ruft sich selbst auf: 4 * 3 * 2 * 1 = 24. Das ist Rekursion (Fakultät).', 'tech': 'Rekursion mit Abbruchbedingung n <= 1.', 'trap': False, 'run': True, 'v': 'both', 'id': 131, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f():\n    return 1, 2\n\nprint(type(f()))', 'p': 'What is the output of the following code?', 'o': ["<class 'int'>", "<class 'list'>", "<class 'tuple'>", 'Error'], 'a': 2, 'kid': 'Zwei Sachen mit Komma zurückgeben = Python packt sie in ein Tupel.', 'tech': 'return a, b liefert ein Tupel.', 'trap': False, 'run': True, 'v': 'both', 'id': 132, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f():\n    return\n    print("x")\n\nprint(f())', 'p': 'What is the output of the following code?', 'o': ['x\nNone', 'None', 'x', 'Error'], 'a': 1, 'kid': 'return beendet die Funktion SOFORT. Das print danach kommt nie dran. Leeres return = None.', 'tech': 'Code nach return ist unerreichbar.', 'trap': False, 'run': True, 'v': 'both', 'id': 133, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'print(print("a"))', 'p': 'What is the output of the following code?', 'o': ['a\na', 'a\nNone', 'None', 'Error'], 'a': 1, 'kid': "Das innere print druckt 'a' und gibt None zurück. Das äußere druckt dann dieses None.", 'tech': 'print() gibt None zurück.', 'trap': True, 'run': True, 'v': 'both', 'id': 134, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f(x):\n    x.append(1)\n\nl = []\nf(l)\nf(l)\nprint(l)', 'p': 'What is the output of the following code?', 'o': ['[]', '[1]', '[1, 1]', 'Error'], 'a': 2, 'kid': 'Die Funktion bekommt die ECHTE Liste (nicht eine Kopie) und kann sie verändern. Zweimal → [1, 1].', 'tech': 'Veränderbare Objekte werden per Referenz geteilt.', 'trap': True, 'run': True, 'v': 'both', 'id': 135, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f(x):\n    x = x + 1\n\na = 5\nf(a)\nprint(a)', 'p': 'What is the output of the following code?', 'o': ['5', '6', 'None', 'Error'], 'a': 0, 'kid': 'Zahlen kann man nicht verändern, nur neu zuweisen – und das passiert nur innen. a bleibt 5.', 'tech': 'int ist immutable; Rebinding wirkt nur lokal.', 'trap': False, 'run': True, 'v': 'both', 'id': 136, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f():\n    pass\n\nprint(f())', 'p': 'What is the output of the following code?', 'o': ['pass', 'None', "''", 'Error'], 'a': 1, 'kid': 'Eine Funktion, die nichts tut, gibt trotzdem was zurück: None.', 'tech': 'Implizites None.', 'trap': False, 'run': True, 'v': 'both', 'id': 137, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'try:\n    print(1 / 0)\nexcept ZeroDivisionError:\n    print("Z")\nexcept:\n    print("E")', 'p': 'What is the output of the following code?', 'o': ['Z', 'E', 'Z\nE', 'ZeroDivisionError'], 'a': 0, 'kid': 'Durch 0 teilen → Fehler. Der erste passende except fängt ihn, die anderen werden ignoriert.', 'tech': 'Nur der erste passende except-Zweig läuft.', 'trap': False, 'run': True, 'v': 'both', 'id': 138, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'try:\n    int("a")\nexcept ValueError:\n    print("V")\nelse:\n    print("OK")\nfinally:\n    print("F")', 'p': 'What is the output of the following code?', 'o': ['V', 'V\nF', 'OK\nF', 'V\nOK\nF'], 'a': 1, 'kid': 'Fehler passiert → except (V). else läuft nur, wenn KEIN Fehler war. finally läuft IMMER.', 'tech': 'try-except-else-finally Reihenfolge.', 'trap': False, 'run': True, 'v': 'both', 'id': 139, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'try:\n    x = [1][2]\nexcept LookupError:\n    print("L")', 'p': 'What is the output of the following code?', 'o': ['L', 'IndexError', 'nothing', 'SyntaxError'], 'a': 0, 'kid': 'IndexError ist ein Kind von LookupError. Wer die Mama fängt, fängt auch die Kinder.', 'tech': 'LookupError ist Basisklasse von IndexError und KeyError.', 'trap': True, 'run': True, 'v': 'both', 'id': 140, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'try:\n    1 / 0\nexcept ArithmeticError:\n    print("A")\nexcept ZeroDivisionError:\n    print("Z")', 'p': 'What is the output of the following code?', 'o': ['A', 'Z', 'A\nZ', 'SyntaxError'], 'a': 0, 'kid': 'ArithmeticError ist die Mama von ZeroDivisionError und steht zuerst – sie fängt alles weg. Der zweite except kommt nie dran.', 'tech': 'Spezifische Exceptions immer VOR allgemeinen. Der erste passende gewinnt.', 'trap': True, 'run': True, 'v': 'both', 'id': 141, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'try:\n    "a" + 1\nexcept TypeError:\n    print("T")\nexcept ValueError:\n    print("V")', 'p': 'What is the output of the following code?', 'o': ['T', 'V', 'T\nV', 'nothing'], 'a': 0, 'kid': 'Text + Zahl → falsche TYPEN → TypeError.', 'tech': 'TypeError: unpassende Typen. ValueError: richtiger Typ, ungültiger Wert.', 'trap': False, 'run': True, 'v': 'both', 'id': 142, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'try:\n    print(y)\nexcept NameError:\n    print("N")', 'p': 'What is the output of the following code?', 'o': ['N', 'None', 'y', 'UnboundLocalError'], 'a': 0, 'kid': 'y wurde nie erschaffen. Python kennt den Namen nicht → NameError.', 'tech': 'Undefinierter Name → NameError.', 'trap': False, 'run': True, 'v': 'both', 'id': 143, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': '', 'p': "Which class is at the top of Python's built-in exception hierarchy?", 'o': ['Exception', 'BaseException', 'ArithmeticError', 'Error'], 'a': 1, 'kid': 'Ganz oben im Stammbaum sitzt die Ur-Oma: BaseException. Darunter erst Exception.', 'tech': 'BaseException → Exception, SystemExit, KeyboardInterrupt ...', 'trap': True, 'run': False, 'v': 'both', 'id': 144, 'de': 'Welche Klasse steht ganz oben an der Spitze des Python-Fehler-Stammbaums (Exception-Hierarchie)?'}, {'b': 4, 'code': '', 'p': 'Which two exceptions are subclasses of LookupError?', 'o': ['ValueError and TypeError', 'IndexError and KeyError', 'ZeroDivisionError and IndexError', 'NameError and KeyError'], 'a': 1, 'kid': "LookupError ist der 'Hab's nicht gefunden'-Fehler: für Listen (IndexError) und Wörterbücher (KeyError).", 'tech': 'LookupError → IndexError, KeyError. ArithmeticError → ZeroDivisionError.', 'trap': False, 'run': False, 'v': 'both', 'id': 145, 'de': 'Welche zwei Fehlerarten sind Unterklassen (Kinder) von LookupError?'}, {'b': 4, 'code': 'try:\n    d = {}\n    d["x"]\nexcept KeyError:\n    print("K")\nexcept LookupError:\n    print("L")', 'p': 'What is the output of the following code?', 'o': ['K', 'L', 'K\nL', 'nothing'], 'a': 0, 'kid': 'Jetzt steht das Kind (KeyError) zuerst – richtig so. Es fängt den Fehler.', 'tech': 'Spezifisch vor allgemein = korrekt.', 'trap': False, 'run': True, 'v': 'both', 'id': 146, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'try:\n    print("A")\nexcept:\n    print("B")\nelse:\n    print("C")', 'p': 'What is the output of the following code?', 'o': ['A', 'A\nC', 'A\nB\nC', 'B'], 'a': 1, 'kid': 'Kein Fehler passiert → except wird übersprungen, else läuft.', 'tech': 'else nach try läuft nur ohne Exception.', 'trap': False, 'run': True, 'v': 'both', 'id': 147, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f(a, b=[]):\n    b.append(a)\n    return b\n\nf(1)\nprint(f(2))', 'p': 'What is the output of the following code?', 'o': ['[2]', '[1, 2]', '[1]', 'Error'], 'a': 1, 'kid': 'Die Standard-Liste wird nur EINMAL gebaut und dann immer wiederverwendet. Die 1 vom ersten Aufruf ist noch drin!', 'tech': 'Veränderbarer Default-Wert wird bei der Definition einmal erzeugt.', 'trap': True, 'run': True, 'v': 'both', 'id': 148, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f(x):\n    return x * 2\n\nprint(f("ab"))', 'p': 'What is the output of the following code?', 'o': ['abab', 'TypeError', 'ab2', 'None'], 'a': 0, 'kid': 'Funktionen sind egal welcher Typ reinkommt: Text mal 2 = Text doppelt.', 'tech': 'Python ist dynamisch typisiert.', 'trap': False, 'run': True, 'v': 'both', 'id': 149, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'def f(a, b, c):\n    return a + b * c\n\nprint(f(1, c=2, b=3))', 'p': 'What is the output of the following code?', 'o': ['7', '9', '5', 'Error'], 'a': 0, 'kid': 'a = 1, b = 3, c = 2. Also 1 + 3 * 2 = 7.', 'tech': 'Gemischte Positions- und Keyword-Argumente.', 'trap': False, 'run': True, 'v': 'both', 'id': 150, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'x = 5\ndef f(x):\n    x += 1\n    return x\n\nprint(f(x), x)', 'p': 'What is the output of the following code?', 'o': ['6 6', '6 5', '5 5', 'Error'], 'a': 1, 'kid': 'Der Parameter x ist ein eigenes, inneres x (Shadowing). Das äußere bleibt 5.', 'tech': 'Parameter sind lokale Variablen.', 'trap': False, 'run': True, 'v': 'both', 'id': 151, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 4, 'code': 'try:\n    l = [1, 2]\n    print(l[5])\nexcept Exception:\n    print("E")\nexcept IndexError:\n    print("I")', 'p': 'What is the output of the following code?', 'o': ['E', 'I', 'E\nI', 'IndexError'], 'a': 0, 'kid': 'Exception ist der Riesen-Kescher, der fast alles fängt. Weil er zuerst steht, bekommt IndexError nie eine Chance.', 'tech': 'Allgemeines except zuerst → spätere Zweige unerreichbar.', 'trap': True, 'run': True, 'v': 'both', 'id': 152, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'import math\nprint(math.ceil(2.1), math.floor(-2.1))', 'p': 'What is the output of the following code?', 'o': ['3 -3', '2 -2', '3 -2', '2 -3'], 'a': 0, 'kid': 'ceil = Decke (immer nach OBEN), floor = Fußboden (immer nach UNTEN). Bei -2.1 ist unten -3!', 'tech': 'ceil/floor runden Richtung +∞ / -∞.', 'trap': True, 'run': True, 'v': '03', 'id': 153, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'import math\nprint(math.trunc(-2.7))', 'p': 'What is the output of the following code?', 'o': ['-3', '-2', '-2.7', '2'], 'a': 1, 'kid': 'trunc schneidet einfach ab, egal ob plus oder minus. -2.7 → -2.', 'tech': 'trunc rundet Richtung 0.', 'trap': False, 'run': True, 'v': '03', 'id': 154, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'import math\nprint(math.sqrt(16))', 'p': 'What is the output of the following code?', 'o': ['4', '4.0', '8', '256'], 'a': 1, 'kid': 'Wurzel aus 16 ist 4 – aber sqrt gibt immer eine Kommazahl.', 'tech': 'math.sqrt liefert float.', 'trap': True, 'run': True, 'v': '03', 'id': 155, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': '', 'p': 'How can you make the random module produce the same sequence of numbers every time the program runs?', 'o': ['random.seed() with the same value', 'random.choice()', 'random.sample()', 'importing random twice'], 'a': 0, 'kid': "seed ist wie ein Startcode für den Zufall. Gleicher Code → gleiche 'Zufalls'-Zahlen, jedes Mal.", 'tech': 'random.seed(n) macht Ergebnisse reproduzierbar.', 'trap': False, 'run': False, 'v': '03', 'id': 156, 'de': 'Wie sorgt man dafür, dass das random-Modul bei jedem Programmstart exakt dieselbe Zahlenfolge erzeugt?'}, {'b': 5, 'code': '', 'p': 'Which function returns several UNIQUE random elements from a sequence?', 'o': ['random.choice()', 'random.sample()', 'random.random()', 'random.seed()'], 'a': 1, 'kid': 'sample zieht wie bei der Lotterie: Jede Kugel kann nur einmal rauskommen.', 'tech': 'random.sample(population, k) → k eindeutige Elemente.', 'trap': False, 'run': False, 'v': '03', 'id': 157, 'de': 'Welche Funktion zieht mehrere EINZIGARTIGE (nicht doppelte) Zufallselemente aus einer Sequenz?'}, {'b': 5, 'code': 'import random\nprint(type(random.random()))', 'p': 'What is the output of the following code?', 'o': ["<class 'int'>", "<class 'float'>", "<class 'bool'>", 'Error'], 'a': 1, 'kid': 'random() gibt immer eine Kommazahl zwischen 0 und 1.', 'tech': 'random.random() ∈ [0.0, 1.0).', 'trap': False, 'run': True, 'v': '03', 'id': 158, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': '', 'p': 'Which open() mode adds new text to the END of an existing file without deleting its content?', 'o': ["'r'", "'w'", "'a'", "'x'"], 'a': 2, 'kid': "a wie 'anhängen' (append). Der alte Inhalt bleibt, das Neue kommt hinten dran.", 'tech': "'w' überschreibt die Datei komplett, 'a' hängt an, 'r' liest nur.", 'trap': True, 'run': False, 'v': '03', 'id': 159, 'de': 'Welcher open()-Modus hängt neuen Text ans ENDE einer bestehenden Datei an, ohne den alten Inhalt zu löschen?'}, {'b': 5, 'code': '', 'p': "What is the main benefit of using 'with open(...) as f:'?", 'o': ['The file is closed automatically', 'The file is deleted', 'The file is read twice', 'Nothing special happens'], 'a': 0, 'kid': 'with ist wie eine Tür mit Automatik: Wenn du den Block verlässt, geht die Datei von selbst zu.', 'tech': 'Context Manager schließt die Datei auch bei Fehlern.', 'trap': False, 'run': False, 'v': '03', 'id': 160, 'de': "Was ist der größte Vorteil, wenn man eine Datei mit 'with open(...) as f:' öffnet?"}, {'b': 5, 'code': '', 'p': 'What happens when you call open("missing.txt", "r") and the file does not exist?', 'o': ['None', 'an empty string', 'FileNotFoundError', 'a new empty file is created'], 'a': 2, 'kid': "Lesen ('r') einer Datei, die es nicht gibt? Python findet sie nicht → FileNotFoundError.", 'tech': "Mit 'w' oder 'a' würde die Datei neu angelegt.", 'trap': False, 'run': False, 'v': '03', 'id': 161, 'de': 'Was passiert beim Aufruf von open("missing.txt", "r"), wenn die Datei gar nicht existiert?'}, {'b': 5, 'code': '', 'p': 'When iterating over csv.reader(f), what is each row?', 'o': ['a list of strings', 'a list of integers', 'a dictionary', 'a single string'], 'a': 0, 'kid': 'csv.reader gibt dir jede Zeile als Liste – und alles darin ist Text, auch Zahlen!', 'tech': 'Werte aus csv.reader sind immer str; zum Rechnen int()/float().', 'trap': True, 'run': False, 'v': '03', 'id': 162, 'de': 'Welchen Datentyp hat jede einzelne Zeile (row), wenn man mit einer Schleife über csv.reader(f) läuft?'}, {'b': 5, 'code': 's = {1, 2, 2, 3}\nprint(len(s))', 'p': 'What is the output of the following code?', 'o': ['4', '3', '2', 'Error'], 'a': 1, 'kid': 'Ein Set ist ein Club, in dem jeder nur EINMAL Mitglied sein darf. Doppelte fliegen raus.', 'tech': 'Sets enthalten keine Duplikate.', 'trap': False, 'run': True, 'v': '03', 'id': 163, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 's = {1, 2, 3}\nprint(s[0])', 'p': 'What is the output of the following code?', 'o': ['1', 'None', 'TypeError', 'IndexError'], 'a': 2, 'kid': 'Ein Set hat keine Platznummern – es ist ein ungeordneter Sack.', 'tech': 'Sets unterstützen keine Indizierung → TypeError.', 'trap': True, 'run': True, 'v': '03', 'id': 164, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'x = {}\nprint(type(x))', 'p': 'What is the output of the following code?', 'o': ["<class 'set'>", "<class 'dict'>", "<class 'list'>", "<class 'tuple'>"], 'a': 1, 'kid': 'Leere geschweifte Klammern sind ein leeres WÖRTERBUCH, kein Set. Leeres Set = set().', 'tech': '{} ist dict; set() ist das leere Set.', 'trap': True, 'run': True, 'v': '03', 'id': 165, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'name = "Bo"\nprint(f"Hi {name}!")', 'p': 'What is the output of the following code?', 'o': ['Hi {name}!', 'Hi Bo!', 'Hi name!', 'Error'], 'a': 1, 'kid': 'Das f vor dem Text heißt: Alles in {} wird ausgetauscht durch den echten Wert.', 'tech': 'f-Strings werten Ausdrücke in {} aus.', 'trap': False, 'run': True, 'v': '03', 'id': 166, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'print("{} + {}".format(1, 2))', 'p': 'What is the output of the following code?', 'o': ['1 + 2', '3', '{} + {}', 'Error'], 'a': 0, 'kid': 'format() füllt die leeren {} der Reihe nach auf. Gerechnet wird nicht.', 'tech': 'str.format setzt Argumente in Platzhalter.', 'trap': False, 'run': True, 'v': '03', 'id': 167, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'print("%d items" % 3)', 'p': 'What is the output of the following code?', 'o': ['3 items', '%d items', 'd items', 'Error'], 'a': 0, 'kid': '%d ist ein alter Platzhalter für eine Ganzzahl.', 'tech': 'Legacy %-Formatierung.', 'trap': False, 'run': True, 'v': '03', 'id': 168, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'def f(*args):\n    print(type(args))\n\nf(1, 2)', 'p': 'What is the output of the following code?', 'o': ["<class 'list'>", "<class 'tuple'>", "<class 'dict'>", "<class 'int'>"], 'a': 1, 'kid': '*args sammelt alle extra Sachen in ein TUPEL ein.', 'tech': '*args → tuple, **kwargs → dict.', 'trap': True, 'run': True, 'v': '03', 'id': 169, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'def f(**kw):\n    print(kw)\n\nf(a=1, b=2)', 'p': 'What is the output of the following code?', 'o': ["{'a': 1, 'b': 2}", '(1, 2)', "[('a', 1), ('b', 2)]", 'Error'], 'a': 0, 'kid': '**kwargs sammelt alle Namens-Argumente in ein Wörterbuch.', 'tech': '**kwargs → dict.', 'trap': False, 'run': True, 'v': '03', 'id': 170, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'if (n := 5) > 3:\n    print(n)', 'p': 'What is the output of the following code?', 'o': ['5', 'True', '3', 'SyntaxError'], 'a': 0, 'kid': ':= ist das Walross 🦭: Es weist zu UND gibt den Wert gleich weiter. n wird 5, und 5 > 3 stimmt.', 'tech': 'Walrus-Operator (Assignment Expression).', 'trap': False, 'run': True, 'v': '03', 'id': 171, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'import math\nprint(math.floor(3.9) + math.ceil(3.1))', 'p': 'What is the output of the following code?', 'o': ['7', '8', '6', '7.0'], 'a': 0, 'kid': 'floor(3.9) = 3, ceil(3.1) = 4. Zusammen 7 (ganze Zahl!).', 'tech': 'floor/ceil geben int zurück.', 'trap': False, 'run': True, 'v': '03', 'id': 172, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 'print("a-b-c".replace("-", ""))', 'p': 'What is the output of the following code?', 'o': ['abc', 'a b c', 'a-b-c', "['a', 'b', 'c']"], 'a': 0, 'kid': "replace tauscht jedes '-' gegen nichts aus.", 'tech': 'replace(alt, neu) ersetzt alle Vorkommen.', 'trap': False, 'run': True, 'v': '03', 'id': 173, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 5, 'code': 's = {1, 2}\ns.add(2)\ns.add(3)\nprint(len(s))', 'p': 'What is the output of the following code?', 'o': ['4', '3', '2', 'Error'], 'a': 1, 'kid': 'Die 2 ist schon im Club, also passiert nichts. Die 3 kommt neu dazu.', 'tech': 'add() ignoriert vorhandene Elemente.', 'trap': False, 'run': True, 'v': '03', 'id': 174, 'de': 'Was gibt der folgende Code auf dem Bildschirm aus?'}, {'b': 1, 'code': 'print(3 % 7 + 7 % 7 + 7 // 3.0)', 'p': 'What is the output of the following code?', 'de': 'Was kommt bei dieser Rechnung mit Modulo (%) und Float-Ganzzahldivision (//) heraus?', 'o': ['5', '5.0', '2.0', '5.33'], 'a': 1, 'kid': '3 % 7 bleibt 3 (weil 7 nullmal in die 3 passt!). 7 % 7 ist 0. Und 7 // 3.0 ist 2.0 (wegen dem .0 wird alles zur Kommazahl!). 3 + 0 + 2.0 = 5.0.', 'tech': 'Ist a < b (positiv), gilt a % b == a. Sobald ein Operand float ist, liefert // ebenfalls ein float (5.0).', 'trap': True, 'run': True, 'v': 'both', 'id': 175}, {'b': 1, 'code': "print(bool('False'), bool(''))", 'p': 'What is the output of the following code?', 'de': "Was gibt bool() für den Text 'False' und für einen leeren Text '' zurück?", 'o': ['False False', 'True False', 'False True', 'True True'], 'a': 1, 'kid': "Reingefallen! 'False' in Anführungszeichen ist ein TEXT mit 5 Buchstaben – die Kiste ist nicht leer, also True! Nur der komplett leere Text '' ist False.", 'tech': "Jeder nicht-leere String (auch 'False' oder '0') ist truthy (True). Nur '' ist falsy (False).", 'trap': True, 'run': True, 'v': 'both', 'id': 176}, {'b': 1, 'code': 'print(round(2.5), round(3.5))', 'p': 'What is the output of the following code?', 'de': 'Wie rundet round() in Python 3, wenn genau .5 hinter dem Komma steht?', 'o': ['3 4', '2 4', '2 3', '3 3'], 'a': 1, 'kid': 'Bei genau .5 rundet Python immer zur nächsten GERADEN Zahl! Bei 2.5 ist die 2 gerade, bei 3.5 ist die 4 gerade -> 2 4.', 'tech': "Banker's Rounding (Round half to even): 2.5 -> 2, 3.5 -> 4.", 'trap': True, 'run': True, 'v': 'both', 'id': 177}, {'b': 1, 'code': "print(chr(ord('A') + 2))", 'p': 'What is the output of the following code?', 'de': "Was machen ord() und chr() mit dem Buchstaben 'A'?", 'o': ['C', 'B', '67', 'TypeError'], 'a': 0, 'kid': "ord('A') holt die Geheimnummer von A im Alphabet (65). Plus 2 sind wir zwei Buchstaben weiter (67), und chr() macht daraus wieder den Buchstaben 'C'!", 'tech': 'ord(char) liefert den Unicode-Codepoint (int), chr(int) wandelt ihn zurück in einen String der Länge 1.', 'trap': False, 'run': True, 'v': 'both', 'id': 178}, {'b': 1, 'code': 'x = 10\ny = 20\nprint(x and y, x or y)', 'p': 'What is the output of the following code?', 'de': "Welchen konkreten Wert geben 'and' und 'or' zurück, wenn man sie mit Zahlen benutzt?", 'o': ['True True', '20 10', '10 20', '10 10'], 'a': 1, 'kid': "'and' prüft x (10 ist wahr) und muss deshalb noch y anschauen -> gibt 20 zurück. 'or' sieht x (10 ist schon wahr!) und hört sofort auf -> gibt 10 zurück!", 'tech': 'x and y liefert x, wenn x falsy ist, sonst y. x or y liefert x, wenn x truthy ist, sonst y.', 'trap': True, 'run': True, 'v': 'both', 'id': 179}, {'b': 2, 'code': 'x = True or (1 / 0 == 0)\nprint(x)', 'p': 'What is the output of the following code?', 'de': "Warum stürzt 1 / 0 auf der rechten Seite von 'or' hier NICHT mit ZeroDivisionError ab?", 'o': ['ZeroDivisionError', 'True', 'False', 'None'], 'a': 1, 'kid': "Python ist faul! Bei 'True or ...' weiß Python schon beim ersten Wort, dass das Ganze True ist. Die rechte Seite mit 1 / 0 wird gar nicht erst angeschaut!", 'tech': 'Short-Circuit Evaluation (Kurzschluss-Auswertung): Bei True or X wird X niemals ausgewertet.', 'trap': True, 'run': True, 'v': 'both', 'id': 180}, {'b': 2, 'code': "vals = [0, '', [], [0], None]\ncount = 0\nfor v in vals:\n    if v:\n        count += 1\nprint(count)", 'p': 'What is the output of the following code?', 'de': "Wie viele Elemente in der Liste vals gelten bei 'if v:' als wahr (True)?", 'o': ['0', '1', '2', '3'], 'a': 1, 'kid': "0, '', [] und None sind alle leer/null (falsch). Aber [0] ist eine Kiste, in der eine 0 liegt – die Kiste selbst ist NICHT leer! Also genau 1 Treffer.", 'tech': '[0] hat len([0]) == 1 und ist damit truthy.', 'trap': True, 'run': True, 'v': 'both', 'id': 181}, {'b': 2, 'code': "for i in range(5, 1):\n    print('*', end='')\nelse:\n    print('*')", 'p': 'How many stars (*) will the following snippet print?', 'de': 'Wie viele Sterne (*) gibt dieser Code mit leerer range(5, 1) und else aus?', 'o': ['0', '1', '4', '5'], 'a': 1, 'kid': 'range(5, 1) läuft 0-mal durch. ABER es gab kein break! Darum läuft der else-Block trotzdem 1-mal und druckt genau 1 Stern.', 'tech': 'Auch bei 0 Schleifendurchläufen wird der else-Zweig ausgeführt, da kein break stattfand.', 'trap': True, 'run': True, 'v': 'both', 'id': 182}, {'b': 2, 'code': "for i in range(3):\n    print(i, end='')\n    i = 99", 'p': 'What is the output of the following code?', 'de': 'Was passiert, wenn man die Schleifenvariable i mitten in einer for-Schleife auf 99 setzt?', 'o': ['09999', '0', '012', '099'], 'a': 2, 'kid': "In der nächsten Runde holt sich 'for' einfach die nächste Zahl aus range(3) und überschreibt deine 99 sofort wieder! Es kommt ganz normal 012 raus.", 'tech': 'Bei jedem Durchlauf weist die for-Schleife i das nächste Element des Iterators neu zu.', 'trap': True, 'run': True, 'v': 'both', 'id': 183}, {'b': 2, 'code': 'x = 8\nx = x << 2\nx = x >> 1\nprint(x)', 'p': 'What is the value of x after the following bit-shift operations?', 'de': 'Welchen Wert hat x nach dem Bit-Verschieben um 2 nach links und 1 nach rechts?', 'o': ['8', '16', '32', '4'], 'a': 1, 'kid': '<< 1 heißt mal 2, also ist 8 << 2 gleich 8 * 2 * 2 = 32. >> 1 heißt durch 2, also 32 >> 1 = 16.', 'tech': '8 << 2 == 32; 32 >> 1 == 16.', 'trap': False, 'run': True, 'v': 'both', 'id': 184}, {'b': 2, 'code': "print(0 or '' or [] or 'Python' or 99)", 'p': 'What is the output of the following code?', 'de': "Was gibt eine Kette von 'or' zurück?", 'o': ['True', 'Python', '99', '0'], 'a': 1, 'kid': "'or' sucht von links nach rechts den ERSTEN Wert, der nicht leer/null ist. 0, '' und [] sind leer, 'Python' ist der erste Treffer!", 'tech': 'Eine or-Kette gibt den ersten truthy Operanden zurück (oder den allerletzten, falls alle falsy sind).', 'trap': True, 'run': True, 'v': 'both', 'id': 185}, {'b': 3, 'code': 't = ([1, 2], 3)\nt[0].append(4)\nprint(t)', 'p': 'What happens when this code runs?', 'de': 'Was passiert, wenn man eine Liste verändert, die IN einem unveränderbaren Tupel steckt?', 'o': ['([1, 2, 4], 3)', 'TypeError', '([1, 2], 3, 4)', 'AttributeError'], 'a': 0, 'kid': 'Das Tupel ist ein versiegelter Glasbehälter, aber DRINNEN liegt ein offener Rucksack (die Liste [1, 2]). In den Rucksack darfst du mit append(4) was reinpacken!', 'tech': 'Tupel sind immutable (Referenzen nicht änderbar), aber veränderbare Elemente im Tupel (wie list) können in-place mutiert werden.', 'trap': True, 'run': True, 'v': 'both', 'id': 186}, {'b': 3, 'code': "items = ['10', '2', '1', '20']\nprint(sorted(items))", 'p': 'What is the output of the following code?', 'de': 'Wie sortiert Python Zahlen, wenn sie als Text (Strings) in Anführungszeichen stehen?', 'o': ["['1', '2', '10', '20']", "['1', '10', '2', '20']", "['20', '10', '2', '1']", 'TypeError'], 'a': 1, 'kid': "Das sind Texte, keine Zahlen! Im Wörterbuch kommt alles mit '1' am Anfang ('1', '10') VOR allem mit '2' am Anfang ('2', '20').", 'tech': 'Lexikografische Sortierung (ASCII/Unicode Zeichen für Zeichen von links nach rechts).', 'trap': True, 'run': True, 'v': 'both', 'id': 187}, {'b': 3, 'code': 'lst = [1, 2, 3]\ndel lst[:]\nprint(lst)', 'p': 'What is the output of the following code?', 'de': 'Was ist der Unterschied zwischen del lst[:] und del lst?', 'o': ['[]', '[1, 2, 3]', 'NameError', 'None'], 'a': 0, 'kid': 'del lst[:] leert nur den Inhalt der Kiste – die leere Kiste [] bleibt stehen! (Erst del lst ohne [:] würde die ganze Kiste vernichten -> NameError).', 'tech': 'del lst[:] löscht alle Elemente in-place (wie lst.clear()); die Variable lst existiert weiter.', 'trap': True, 'run': True, 'v': 'both', 'id': 188}, {'b': 3, 'code': 'matrix = [[i + j for i in range(2)] for j in range(2)]\nprint(matrix[1][0])', 'p': 'What is the output of the following code?', 'de': 'Welcher Wert steht in dieser verschachtelten List Comprehension auf Platz [1][0]?', 'o': ['0', '1', '2', 'IndexError'], 'a': 1, 'kid': 'Für j=0 entsteht [0, 1], für j=1 entsteht [1, 2]. matrix[1] ist die zweite Liste [1, 2], und davon Platz 0 ist die 1.', 'tech': 'matrix == [[0, 1], [1, 2]], daher ist matrix[1][0] == 1.', 'trap': True, 'run': True, 'v': 'both', 'id': 189}, {'b': 3, 'code': 'lst = [1, 2, 3]\nlst.insert(0, 9)\ndel lst[2]\nprint(lst)', 'p': 'What is the output of the following code?', 'de': 'Was steht nach insert(0, 9) und del lst[2] in der Liste?', 'o': ['[9, 1, 3]', '[9, 2, 3]', '[1, 9, 3]', '[9, 1, 2]'], 'a': 0, 'kid': 'Erst drängelt sich die 9 auf Platz 0 -> [9, 1, 2, 3]. Jetzt ist auf Platz 2 die 2! Die wird gelöscht -> [9, 1, 3].', 'tech': 'Durch insert(0, 9) verschieben sich alle Indizes um +1.', 'trap': True, 'run': True, 'v': 'both', 'id': 190}, {'b': 3, 'code': 'a, b = 1, 2\na, b = b, a + b\nprint(a, b)', 'p': 'What is the output of the following code?', 'de': 'Was passiert bei gleichzeitiger Zuweisung a, b = b, a + b?', 'o': ['2 3', '2 4', '1 3', '3 2'], 'a': 0, 'kid': 'Python rechnet ERST rechts komplett mit den alten Zahlen: b ist 2, und a + b ist 1 + 2 = 3. Dann erst kriegen a und b die neuen Werte: 2 3.', 'tech': 'Tuple-Assignment wertet erst die komplette rechte Seite als Tupel (2, 3) aus und entpackt sie dann nach links.', 'trap': True, 'run': True, 'v': 'both', 'id': 191}, {'b': 3, 'code': 'x = [1, 2]\ny = x\nx = x + [3]\nprint(y)', 'p': 'What is the output of the following code?', 'de': 'Achtung Mega-Falle: Was ist der Unterschied zwischen x = x + [3] und x += [3]?', 'o': ['[1, 2]', '[1, 2, 3]', '[3]', 'Error'], 'a': 0, 'kid': 'x + [3] baut eine KOMPLETT NEUE Kiste für x! y schaut aber noch auf die alte Kiste [1, 2]. (Nur bei x += [3] oder x.append(3) hätte sich auch y geändert!).', 'tech': 'x = x + [3] erzeugt ein neues Listen-Objekt und bindet nur x neu; y referenziert weiter die ursprüngliche Liste [1, 2].', 'trap': True, 'run': True, 'v': 'both', 'id': 192}, {'b': 3, 'code': "d = {1: 'a', True: 'b', 1.0: 'c'}\nprint(len(d), d[1])", 'p': 'What is the output of the following code?', 'de': 'Was passiert in einem Dictionary, wenn die Keys 1, True und 1.0 heißen?', 'o': ['3 a', '1 c', '3 c', '2 b'], 'a': 1, 'kid': "Für Python sind 1, True und 1.0 exakt GLEICH (1 == True == 1.0)! Sie teilen sich dieselbe Schublade, und jeder neue Wert überschreibt den alten -> 1 Schublade mit 'c'!", 'tech': "Da 1 == True == 1.0 und deren Hashes identisch sind, existiert nur 1 Key im Dict; der Wert wird zuletzt mit 'c' überschrieben.", 'trap': True, 'run': True, 'v': 'both', 'id': 193}, {'b': 3, 'code': "print('a' in 'abc', 'ac' in 'abc')", 'p': 'What is the output of the following code?', 'de': "Was prüft 'in' bei einem String?", 'o': ['True True', 'True False', 'False False', 'TypeError'], 'a': 1, 'kid': "'in' sucht bei Texten nach einem zusammenhängenden Stück! 'a' klebt drin, aber zwischen 'a' und 'c' steht noch das 'b' im Weg -> True False.", 'tech': 'Substring-Prüfung mit in erfordert eine zusammenhängende Zeichenfolge.', 'trap': True, 'run': True, 'v': 'both', 'id': 194}, {'b': 3, 'code': "d = {'x': 10, 'y': 20}\nprint(list(d))", 'p': 'What is the output of the following code?', 'de': 'Was kommt heraus, wenn man ein Dictionary in list() steckt?', 'o': ["['x', 'y']", '[10, 20]', "[('x', 10), ('y', 20)]", 'TypeError'], 'a': 0, 'kid': 'Wenn du über ein Wörterbuch läufst oder list(d) machst, bekommst du immer nur die SCHLÜSSEL (Keys)!', 'tech': 'Iteration über ein dict liefert standardmäßig dessen Keys.', 'trap': False, 'run': True, 'v': 'both', 'id': 195}, {'b': 4, 'code': 'def f():\n    try:\n        return 1\n    finally:\n        return 2\n\nprint(f())', 'p': 'What is the output of the following code?', 'de': 'Wer gewinnt, wenn sowohl im try-Block als auch im finally-Block ein return steht?', 'o': ['1', '2', '1\n2', 'SyntaxError'], 'a': 1, 'kid': 'finally hat immer das letzte Wort! Bevor die 1 rausgehen kann, grätscht finally dazwischen und gibt die 2 zurück.', 'tech': 'Ein return im finally-Block überschreibt jedes vorherige return oder jede Exception aus dem try-Block.', 'trap': True, 'run': True, 'v': 'both', 'id': 196}, {'b': 4, 'code': "try:\n    x = int('abc')\nexcept (ZeroDivisionError, ValueError):\n    print('Caught')", 'p': 'What is the output of the following code?', 'de': 'Kann ein einziger except-Block mehrere Fehlertypen in einem Tupel abfangen?', 'o': ['Caught', 'ValueError', 'SyntaxError', 'TypeError'], 'a': 0, 'kid': 'Ja! Mit runden Klammern (Fehler1, Fehler2) kann ein einziger except-Wächter gleich mehrere Fehlertypen fangen.', 'tech': 'except (Exc1, Exc2): fängt alle im Tupel genannten Exception-Klassen ab.', 'trap': False, 'run': True, 'v': 'both', 'id': 197}, {'b': 4, 'code': 'x = [1, 2]\ndef f(lst):\n    lst = [9, 9]\n\nf(x)\nprint(x)', 'p': 'What is the output of the following code?', 'de': 'Ändert sich die Liste x draußen, wenn der Parameter lst in der Funktion komplett neu zugewiesen wird (lst = [9, 9])?', 'o': ['[9, 9]', '[1, 2]', 'None', 'Error'], 'a': 1, 'kid': 'Aufgepasst! lst.append() würde die echte Kiste ändern. Aber lst = [9, 9] klebt das Namensschild lst innen nur auf eine neue Kiste. Draußen bleibt x bei [1, 2]!', 'tech': 'Neuzuweisung eines Parameters (lst = ...) bindet nur den lokalen Namen um und verändert das übergebene Objekt nicht.', 'trap': True, 'run': True, 'v': 'both', 'id': 198}, {'b': 4, 'code': 'def calc(a, b=2, c=3):\n    return a + b * c\n\nprint(calc(1, c=10))', 'p': 'What is the output of the following code?', 'de': 'Welches Ergebnis liefert calc(1, c=10), wenn b seinen Standardwert behält?', 'o': ['21', '30', '13', 'TypeError'], 'a': 0, 'kid': 'a bekommt die 1, b wird ausgelassen und behält seinen Standardwert 2, und c bekommt 10. Punkt vor Strich: 1 + (2 * 10) = 21!', 'tech': 'a=1 (positional), b=2 (default), c=10 (keyword) -> 1 + 2*10 = 21.', 'trap': False, 'run': True, 'v': 'both', 'id': 199}]

BLOCKS = {
    1: "🧮 Block 1: Grundlagen & Mathe (18%)",
    2: "🔁 Block 2: if, Schleifen & range (29%)",
    3: "📦 Block 3: Listen, Tupel, Dicts, Strings (25%)",
    4: "🧯 Block 4: Funktionen & Exceptions (28%)",
    5: "📁 Block 5: Dateien, Module, Sets (nur 30-03)"
}

RIGHT_MSGS = [
    "Jaaa! Gehirnzelle Nr. 3 hat gezündet 🧠⚡",
    "BOOM 💥 Python-Flüsterer im Haus!",
    "Korrekt, du kleines Genie 🤓",
    "Sauber! Die Kohlenstoffeinheit vom Planeten Dumbia lernt 🧬🚀",
    "Richtig! Die Schlange verneigt sich 🐍🙇",
    "Zack, sitzt! Wie ein Keks im Kakao 🍪",
    "Exakt. Der OpenEDG-Prüfer weint gerade leise 😭",
    "Wassergehirn? Eher Turbogehirn! 🚀"
]

WRONG_MSGS = [
    "Nööö! Deine Kohlenstoffeinheit hat einen Wasserschaden 💦",
    "Falsch, du verwirrte Kartoffel 🥔 – ab in die Fehler-Kiste!",
    "Bruder… nein. Einfach nein. 🙅",
    "Das Wassergehirn hat geblubbert, aber nicht gedacht 🫧",
    "Python lacht dich gerade ganz leise aus 🐍😏",
    "Autsch! Falle gesehen, trotzdem reingehüpft 🪤",
    "Du Pommes ohne Ketchup 🍟 — lies die 5-Jährigen-Erklärung!"
]

CHEAT_TEXT = """📜 DIE 25 TÖDLICHSTEN PCEP-FALLEN & 🇬🇧 ENGLISCH-ÜBERLEBENS-WÖRTERBUCH
================================================================================

🇬🇧 TEIL 1: ENGLISCH-WÖRTERBUCH FÜR DIE PRÜFUNG
--------------------------------------------------------------------------------
• "What is the expected output of the following snippet?" -> Was gibt der Code aus?
• "The code will raise an exception / runtime error"      -> Der Code stürzt mit Fehler ab!
• "The program will enter an infinite loop"               -> Endlosschleife!
• "mutable" vs. "immutable"                               -> veränderbar (list, dict) vs. unveränderbar (tuple, str)
• "positional argument" vs. "keyword argument"            -> f(1, 2) vs. f(a=1, b=2)

⚡ TEIL 2: BLOCK 1 – MATHE & BASICS (18%)
--------------------------------------------------------------------------------
1. Normales Teilen (/) ergibt IMMER float: 7 / 7 -> 1.0 (nie 1!)
2. Ganzzahl-Division (//) rundet nach UNTEN: 7 // 2 -> 3, aber -7 // 2 -> -4!
3. Modulo (%) hat das Vorzeichen der rechten Zahl: -7 % 3 -> 2. Und 3 % 7 -> 3!
4. Potenz (**) rechnet von RECHTS nach LINKS: 2 ** 3 ** 2 = 2 ** 9 = 512! Und -2 ** 2 = -4!
5. ^ ist XOR (unterschiedlich = 1), NICHT Potenz! ~x ist immer -x - 1 (~5 -> -6).
6. input() liefert IMMER einen Text (str): '5' * 2 -> '55'. int('3.5') -> ValueError!
7. True == 1, False == 0: True + True -> 2. Aber bool('False') -> True (nicht-leerer Text!).

🔁 TEIL 3: BLOCK 2 – SCHLEIFEN & LOGIK (29%)
--------------------------------------------------------------------------------
8. range(start, stop, step): stop ist NIE dabei! range(5, 1) ist leer (0 Durchläufe).
9. else: nach for/while wird IMMER ausgeführt, AUSSER es gab ein break!
10. Logik-Rangfolge: Erst not, dann and, zuletzt or!
11. Falsy (gelten als False): 0, 0.0, '', [], (), {}, None. Aber [0] ist True!

📦 TEIL 4: BLOCK 3 – LISTEN, TUPEL, DICTS & STRINGS (25%)
--------------------------------------------------------------------------------
12. Zwillings-Falle: b = a kopiert KEINE Liste! Echte Kopie: b = a[:] oder a.copy().
13. (5) ist nur int, erst mit Komma (5,) ist es ein Tupel! {} ist ein dict (leeres Set: set()).
14. Slicing wirft nie IndexError: l[10:100] -> [], aber l[100] -> IndexError!
15. l.sort() gibt None zurück! sorted(l) gibt eine neue sortierte Liste zurück.
16. Strings & Tupel sind immutable: s[0] = 'A' -> TypeError!
17. Im Dictionary sind 1, True und 1.0 derselbe Key: len({1:'a', True:'b', 1.0:'c'}) -> 1!

🧯 TEIL 5: BLOCK 4 – FUNKTIONEN & EXCEPTIONS (28%)
--------------------------------------------------------------------------------
18. Jede Funktion ohne return (oder mit leerem return) gibt None zurück!
19. Erst Positional Arguments (ohne =), danach Keyword Arguments (mit =). Sonst SyntaxError!
20. Exception-Stammbaum:
    BaseException -> Exception -> ArithmeticError -> ZeroDivisionError
                               -> LookupError     -> IndexError & KeyError
"""


class PCEPTrainerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🐍 PCEP Gehirn-Trainer Ultimate – Kohlenstoffeinheiten-Edition (200 Fragen)")
        self.geometry("1080x820")
        self.minsize(920, 700)
        self.configure(bg="#12141d")

        self.save_file = Path(__file__).with_name("pcep_fortschritt.json")
        self.ver = "02"
        self.wrong_box = set()
        self.mastered = set()
        self.streak = 0
        self.show_de = False
        self.load_progress()

        self.active_questions = []
        self.q_idx = 0
        self.score = 0
        self.answered_count = 0
        self.current_answered = False
        self.is_exam = False
        self.exam_seconds = 0
        self.timer_job = None
        self.mode_name = "Alle Fragen"

        self._build_ui()
        self.start_mode("ALL")

    def load_progress(self):
        if self.save_file.exists():
            try:
                data = json.loads(self.save_file.read_text(encoding="utf-8"))
                self.ver = data.get("ver", "02")
                self.wrong_box = set(data.get("wrong_box", []))
                self.mastered = set(data.get("mastered", []))
                self.streak = data.get("streak", 0)
            except Exception:
                pass

    def save_progress(self):
        try:
            data = {
                "ver": self.ver,
                "wrong_box": sorted(list(self.wrong_box)),
                "mastered": sorted(list(self.mastered)),
                "streak": self.streak
            }
            self.save_file.write_text(json.dumps(data, indent=2), encoding="utf-8")
        except Exception:
            pass

    def get_pool(self):
        return [q for q in BANK if self.ver == "03" or q.get("v") != "03"]

    def get_rank_title(self):
        m = len(self.mastered)
        if m < 10:
            return f"🥔 Verwirrte Kartoffel ({m})"
        elif m < 30:
            return f"🫧 Wassergehirn ({m})"
        elif m < 65:
            return f"🧬 Kohlenstoffeinheit ({m})"
        elif m < 110:
            return f"⚔️ Python-Padawan ({m})"
        return f"🧙‍♂️ PCEP Jedi-Meister ({m})"

    def _build_ui(self):
        # Top Header
        hdr = tk.Frame(self, bg="#1b1f2e", padx=18, pady=12)
        hdr.pack(fill="x")

        tk.Label(
            hdr,
            text="🐍 PCEP Gehirn-Trainer Ultimate (200 Fragen)",
            font=("Segoe UI", 16, "bold"),
            bg="#1b1f2e",
            fg="#ffd23f"
        ).pack(side="left")

        self.lbl_rank = tk.Label(
            hdr,
            text="",
            font=("Segoe UI", 10, "bold"),
            bg="#24293e",
            fg="#3ddc84",
            padx=10,
            pady=4
        )
        self.lbl_rank.pack(side="left", padx=12)

        self.btn_ver = tk.Button(
            hdr,
            text="Version: PCEP-30-02 (WBS)",
            command=self.toggle_version,
            font=("Segoe UI", 9, "bold"),
            bg="#ffd23f",
            fg="#111111",
            relief="flat",
            padx=10,
            pady=5
        )
        self.btn_ver.pack(side="right", padx=4)

        tk.Button(
            hdr,
            text="📜 Spickzettel & 🇬🇧 Wörterbuch",
            command=self.open_cheatsheet,
            font=("Segoe UI", 9, "bold"),
            bg="#26c6da",
            fg="#111111",
            relief="flat",
            padx=10,
            pady=5
        ).pack(side="right", padx=4)

        tk.Button(
            hdr,
            text="🎓 30-Fragen Prüfungssimulation",
            command=lambda: self.start_mode("EXAM"),
            font=("Segoe UI", 9, "bold"),
            bg="#ff9f43",
            fg="#111111",
            relief="flat",
            padx=10,
            pady=5
        ).pack(side="right", padx=4)

        # Filter & Mode Bar
        fbar = tk.Frame(self, bg="#12141d", padx=18, pady=8)
        fbar.pack(fill="x")

        modes = [
            ("ALL", "🎲 Alle"),
            ("1", "🧮 Block 1 (18%)"),
            ("2", "🔁 Block 2 (29%)"),
            ("3", "📦 Block 3 (25%)"),
            ("4", "🧯 Block 4 (28%)"),
            ("5", "📁 Block 5 (30-03)"),
            ("TRAP", "🪤 Nur Fangfragen"),
            ("BOX", "📦 Fehler-Kiste")
        ]
        self.mode_btns = {}
        for code, label in modes:
            b = tk.Button(
                fbar,
                text=label,
                command=lambda c=code: self.start_mode(c),
                font=("Segoe UI", 9, "bold"),
                bg="#24293e",
                fg="#eef0f7",
                relief="flat",
                padx=8,
                pady=4
            )
            b.pack(side="left", padx=3)
            self.mode_btns[code] = b

        self.lbl_stats = tk.Label(
            fbar,
            text="",
            font=("Segoe UI", 10, "bold"),
            bg="#12141d",
            fg="#3ddc84"
        )
        self.lbl_stats.pack(side="right")

        # Main Card
        self.card = tk.Frame(self, bg="#1b1f2e", padx=22, pady=16)
        self.card.pack(fill="both", expand=True, padx=18, pady=(0, 14))

        meta = tk.Frame(self.card, bg="#1b1f2e")
        meta.pack(fill="x")

        self.lbl_badge = tk.Label(meta, text="", font=("Segoe UI", 10, "bold"), bg="#24293e", fg="#7cc4ff", padx=8, pady=3)
        self.lbl_badge.pack(side="left")

        self.lbl_trap = tk.Label(meta, text="🪤 FIESE PCEP-FANGFRAGE!", font=("Segoe UI", 9, "bold"), bg="#ff9f43", fg="#111111", padx=8, pady=3)

        tk.Button(
            meta,
            text="🇩🇪 Frage auf Deutsch übersetzen",
            command=self.toggle_de_hint,
            font=("Segoe UI", 9, "bold"),
            bg="#24293e",
            fg="#26c6da",
            relief="flat",
            padx=10,
            pady=3
        ).pack(side="right")

        self.lbl_q_en = tk.Label(
            self.card,
            text="",
            font=("Segoe UI", 13, "bold"),
            bg="#1b1f2e",
            fg="#ffffff",
            wraplength=980,
            justify="left",
            anchor="w"
        )
        self.lbl_q_en.pack(fill="x", pady=(10, 4))

        self.lbl_q_de = tk.Label(
            self.card,
            text="",
            font=("Segoe UI", 10, "bold"),
            bg="#16323d",
            fg="#9ef5ff",
            wraplength=980,
            justify="left",
            anchor="w",
            padx=10,
            pady=6
        )

        self.txt_code = tk.Text(
            self.card,
            height=6,
            font=("Consolas", 12),
            bg="#0b0d14",
            fg="#eef0f7",
            bd=0,
            padx=12,
            pady=10,
            wrap="none"
        )
        self.txt_code.pack(fill="x", pady=8)

        self.opts_frame = tk.Frame(self.card, bg="#1b1f2e")
        self.opts_frame.pack(fill="x", pady=4)

        self.opt_buttons = []
        for i in range(4):
            btn = tk.Button(
                self.opts_frame,
                text="",
                command=lambda idx=i: self.answer_question(idx),
                font=("Consolas", 11),
                bg="#24293e",
                fg="#eef0f7",
                activebackground="#353c59",
                activeforeground="#ffffff",
                relief="flat",
                anchor="w",
                justify="left",
                padx=14,
                pady=8
            )
            btn.pack(fill="x", pady=3)
            self.opt_buttons.append(btn)

        # Nav Bar
        nav = tk.Frame(self.card, bg="#1b1f2e", pady=8)
        nav.pack(fill="x")

        tk.Button(
            nav,
            text="← Vorherige Frage",
            command=self.prev_q,
            font=("Segoe UI", 10, "bold"),
            bg="#24293e",
            fg="#eef0f7",
            relief="flat",
            padx=12,
            pady=6
        ).pack(side="left", padx=(0, 8))

        tk.Button(
            nav,
            text="Nächste Frage → (Enter)",
            command=self.next_q,
            font=("Segoe UI", 10, "bold"),
            bg="#ffd23f",
            fg="#111111",
            relief="flat",
            padx=14,
            pady=6
        ).pack(side="left")

        # Explanation Box
        self.exp_frame = tk.Frame(self.card, bg="#162925", padx=14, pady=10)
        self.lbl_exp_head = tk.Label(self.exp_frame, text="", font=("Segoe UI", 12, "bold"), bg="#162925", fg="#3ddc84", anchor="w")
        self.lbl_exp_head.pack(fill="x")
        self.lbl_exp_kid = tk.Label(self.exp_frame, text="", font=("Segoe UI", 10), bg="#162925", fg="#ffffff", wraplength=960, justify="left", anchor="w")
        self.lbl_exp_kid.pack(fill="x", pady=(4, 2))
        self.lbl_exp_tech = tk.Label(self.exp_frame, text="", font=("Segoe UI", 10, "bold"), bg="#162925", fg="#ffd23f", wraplength=960, justify="left", anchor="w")
        self.lbl_exp_tech.pack(fill="x", pady=(2, 0))

        self.bind("<Return>", lambda e: self.next_q())
        for k, idx in [("1", 0), ("2", 1), ("3", 2), ("4", 3), ("a", 0), ("b", 1), ("c", 2), ("d", 3)]:
            self.bind(k, lambda e, i=idx: self.answer_question(i))

    def toggle_version(self):
        self.ver = "03" if self.ver == "02" else "02"
        self.btn_ver.configure(text=f"Version: PCEP-30-{self.ver}")
        self.save_progress()
        self.start_mode("ALL")

    def toggle_de_hint(self):
        if self.lbl_q_de.winfo_ismapped():
            self.lbl_q_de.pack_forget()
        else:
            self.lbl_q_de.pack(fill="x", pady=(0, 6), before=self.txt_code)

    def start_mode(self, mode):
        if self.timer_job:
            self.after_cancel(self.timer_job)
            self.timer_job = None
        self.is_exam = False

        pool = self.get_pool()
        if mode == "ALL":
            qs = list(pool)
            random.shuffle(qs)
            self.mode_name = "🎲 Alle Fragen"
        elif mode == "TRAP":
            qs = [q for q in pool if q.get("trap")]
            random.shuffle(qs)
            self.mode_name = "🪤 Nur Fangfragen"
        elif mode == "BOX":
            qs = [q for q in pool if q["id"] in self.wrong_box]
            if not qs:
                messagebox.showinfo("Fehler-Kiste leer 🎉", "Deine Fehler-Kiste ist komplett leer! Du hast aktuell keine offenen Fehler.")
                return
            random.shuffle(qs)
            self.mode_name = f"📦 Fehler-Kiste ({len(qs)})"
        elif mode == "EXAM":
            self.is_exam = True
            total = 30 if self.ver == "02" else 35
            qs = list(pool)
            random.shuffle(qs)
            qs = qs[:total]
            self.exam_seconds = (40 if self.ver == "02" else 50) * 60
            self.mode_name = f"🎓 Prüfungssimulation ({total} Fragen)"
            self._tick_exam()
        else:
            b_num = int(mode)
            if b_num == 5 and self.ver == "02":
                self.ver = "03"
                self.btn_ver.configure(text="Version: PCEP-30-03")
                pool = self.get_pool()
            qs = [q for q in pool if q["b"] == b_num]
            random.shuffle(qs)
            self.mode_name = f"Block {b_num}"

        self.active_questions = qs
        self.q_idx = 0
        self.score = 0
        self.answered_count = 0
        self.render_current()

    def _tick_exam(self):
        if not self.is_exam:
            return
        self.exam_seconds -= 1
        if self.exam_seconds <= 0:
            self.is_exam = False
            pct = round(self.score / max(1, len(self.active_questions)) * 100)
            messagebox.showinfo("Zeit abgelaufen!", f"Ergebnis: {self.score}/{len(self.active_questions)} ({pct}%)")
            return
        self.update_header_stats()
        self.timer_job = self.after(1000, self._tick_exam)

    def update_header_stats(self):
        self.lbl_rank.configure(text=f"{self.get_rank_title()}  |  🔥 Streak: {self.streak}")
        self.mode_btns["BOX"].configure(text=f"📦 Fehler-Kiste ({len(self.wrong_box)})")
        timer_str = ""
        if self.is_exam:
            m, s = divmod(self.exam_seconds, 60)
            timer_str = f"⏱️ {m:02d}:{s:02d}  |  "
        self.lbl_stats.configure(
            text=f"{timer_str}{self.mode_name}  |  ✅ {self.score}/{self.answered_count}  |  Frage {self.q_idx + 1}/{len(self.active_questions)}"
        )

    def render_current(self):
        q = self.active_questions[self.q_idx]
        self.current_answered = False
        self.update_header_stats()

        self.lbl_badge.configure(text=BLOCKS.get(q["b"], f"Block {q['b']}"))
        if q.get("trap"):
            self.lbl_trap.pack(side="left", padx=8)
        else:
            self.lbl_trap.pack_forget()

        self.lbl_q_en.configure(text=f"Q{self.q_idx + 1}: {q['p']}")
        self.lbl_q_de.configure(text=f"🇩🇪 Auf Deutsch: {q.get('de', '')}")
        self.lbl_q_de.pack_forget()

        self.txt_code.configure(state="normal")
        self.txt_code.delete("1.0", "end")
        code_text = q.get("code") or "# (Theorie-Frage ohne Code-Schnipsel)"
        self.txt_code.insert("1.0", code_text)
        self.txt_code.configure(state="disabled")

        for i, opt_btn in enumerate(self.opt_buttons):
            letter = "ABCD"[i]
            opt_btn.configure(
                text=f"  [{letter}]   {q['o'][i]}",
                bg="#24293e",
                fg="#eef0f7",
                state="normal"
            )

        self.exp_frame.pack_forget()

    def answer_question(self, chosen_idx):
        if self.current_answered:
            return
        self.current_answered = True
        q = self.active_questions[self.q_idx]
        correct_idx = q["a"]
        ok = (chosen_idx == correct_idx)

        self.answered_count += 1
        if ok:
            self.score += 1
            self.streak += 1
            self.mastered.add(q["id"])
            if q["id"] in self.wrong_box:
                self.wrong_box.remove(q["id"])
        else:
            self.streak = 0
            self.wrong_box.add(q["id"])

        self.save_progress()
        self.update_header_stats()

        for i, btn in enumerate(self.opt_buttons):
            if i == correct_idx:
                btn.configure(bg="#1b4332", fg="#3ddc84")
            elif i == chosen_idx and not ok:
                btn.configure(bg="#4a1525", fg="#ff5d73")

        bg_col = "#162925" if ok else "#381822"
        self.exp_frame.configure(bg=bg_col)
        self.lbl_exp_head.configure(
            bg=bg_col,
            fg="#3ddc84" if ok else "#ff5d73",
            text=random.choice(RIGHT_MSGS if ok else WRONG_MSGS)
        )
        self.lbl_exp_kid.configure(bg=bg_col, text=f"👶 Für 5-Jährige: {q['kid']}")
        self.lbl_exp_tech.configure(bg=bg_col, text=f"🤓 Profi-Regel: {q['tech']}")
        self.exp_frame.pack(fill="x", pady=(8, 0))

    def next_q(self):
        if self.q_idx < len(self.active_questions) - 1:
            self.q_idx += 1
            self.render_current()
        else:
            pct = round(self.score / max(1, self.answered_count) * 100)
            messagebox.showinfo(
                "Runde abgeschlossen! 🏁",
                f"Du hast {self.score} von {self.answered_count} Fragen richtig ({pct}%).\n"
                f"{'🎉 BESTANDEN-NIVEAU (≥ 70%)!' if pct >= 70 else '💪 Ab in die Fehler-Kiste zum Wiederholen!'}"
            )

    def prev_q(self):
        if self.q_idx > 0:
            self.q_idx -= 1
            self.render_current()

    def open_cheatsheet(self):
        win = tk.Toplevel(self)
        win.title("📜 PCEP Spickzettel & 🇬🇧 Englisch-Überlebens-Wörterbuch")
        win.geometry("880x680")
        win.configure(bg="#12141d")
        txt = tk.Text(win, font=("Consolas", 11), bg="#1b1f2e", fg="#eef0f7", padx=18, pady=18, wrap="word")
        txt.pack(fill="both", expand=True, padx=14, pady=14)
        txt.insert("1.0", CHEAT_TEXT)
        txt.configure(state="disabled")


if __name__ == "__main__":
    app = PCEPTrainerApp()
    app.mainloop()
