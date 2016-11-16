# big5trait module

### 使用方法
	from big5trait import big5trait
	big5trait(要分類的字詞清單, 性格參數, 容許值)

##### Parameter

* 要分類的字詞清單 : list of string

	一個list of string, 放入所有要判定的詞

* 性格參數 : list of float

	要判定的性格的big5參數值，順序是:

	1. Extraversion

	1. Emotional stability

	1. Agreeableness

	1. Conscientiousness

	1. Openness to experience

* 容許值 : float

	性格參數的容許值

##### Return
	{
		"passed" : 符合此性格的字詞list,
		"failed" : 不符合此性格的字詞list
	}

**HashDict必須和big5trait.py在同一個資料夾**

### 檔案說明

* big5trait.py : big5trait模組檔

* HashDict : hash過的字典

* cliwc.dic : 繁體中文LIWC字典檔

* dic2trait.py : 從LIWC字典檔轉為性格參數

* hashgen.py : 產生hash字典用
