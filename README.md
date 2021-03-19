# Клавиатурный runner

Код представляет собой основную механику игры. А именно - реакция на ввод с клавиатуры и смена активного символа.

Часть информации выводится в консоль.

Ваша задача:

1. В основное окно *root* добавить информацию о:
	1. текущей раскладке (английская или русская)
	1. к-к-комбо (количество символов введенных без ошибки)
	1. процент корректности (отношение между правильно введенными символами и общим количеством введенных)
	1. если символ введен неправильно, поле символа должно поменять фон на красный, при правильно введенном символе, поле возвращает свой цвет
1. Ответить на вопросы:
	1. зачем нужны строки 5, 6:
```python
if event.keysym in ["Shift_L", "Shift_R", "Control_L", "Control_L", "Alt_L", "Alt_R"]:
	return False
```
	1. какие строки отвечают за перехват события нажатия клавиши
	1. как происходит перехват и сравнение символа введенного с клавиатуры