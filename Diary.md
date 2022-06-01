# 雑記

initがコンストラクタの役割をもつことについては理解したが、引数にselfが入っている意味が???である
ないとどうなるんだろう
あと、もしかしたら違うかもしれないがメソッドの使い方がJavaと違うような気がする。
Javaだと(Sample.)foo.bar()は(Sample"クラス"に入っている)foo"フィールド"のbar"関数"を呼ぶことを表すが  
Pythonだとfoo.bar()はfoo"インスタンス"のbar"関数"を呼ぶことを表す  
と認識してる（いい例が思い浮かばなかった...）

DynamoDBについてSDKを用いたCreateTableの仕方は偶然分かったが、create_tableメソッド中のself引数の意味がよくわからなかった。
> BOOL、L、M、N、NS、S、SS などのデータ型記述子は、JSON データ形式でのデータ型に対応します。  
> https://docs.aws.amazon.com/ja_jp/sdk-for-net/v3/developer-guide/dynamodb-expressions.html

らしい。また、

> The following is a complete list of DynamoDB data type descriptors:  
> S – String  
> N – Number  
> B – Binary  
> BOOL – Boolean  
> NULL – Null  
> M – Map  
> L – List  
> SS – String Set  
> NS – Number Set  
> BS – Binary Set  
> https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Programming.LowLevelAPI.html

らしい。

今回はDayにはN、WhereにはSを使おうと思う。Dayはyyyymmdd形式、Whereは部位（Chest、Legなど）を想定しているため。
add_tableはうまく使えてないため明日以降検証