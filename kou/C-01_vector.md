---
title: 【質問】イッチ、交点のベクトルを求めようとしたら比がどこにも書いてなくて詰む
unit: 数C・ベクトル
goal: 平面・空間のベクトルを「一次独立なベクトルの和」で表し、交点を係数比較で、長さを内積で求められるようになる
prereq: ベクトルの演算・成分・内積（前スレ）、内分点（数A・数II）、連立方程式、三角比、展開
core: 平面のベクトルは全部「2本の基準のベクトル」で書ける。同じ点を2通りに表して係数比較
---

@1 イッチ
ベクトルの宿題これ
△OAB で、辺 OA を $2:1$ に内分する点を C、辺 OB の中点を D とする
線分 AD と BC の交点を P とするとき、$\overrightarrow{OP}$ を $\vec{a}=\overrightarrow{OA}$, $\vec{b}=\overrightarrow{OB}$ で表せ
図は描いた。で、何すればええの？

@2 名無し
うぽつ
図描いただけ偉い

@3 イッチ
P って「なんか真ん中らへん」としか言えんのやが
定規で測ったらあかん？

@4 名無し
>>3
定規ベクトル民で草

@5 名無し
測っても $\frac{1}{2}$ とかぴったりにはならんやろ

@6 古参ニキ
>>1
ベクトルの交点、通称「文字が増える問題」やな
いきなり式をいじる前に聞くで
**この問題、どこがウザい？**

@7 イッチ
>>6
P の場所の情報がないとこ
C とか D は「何対何」って書いてあるのに、P だけ何も書いてない

@8 古参ニキ
>>7
ええとこ見とる
「情報がない点」をどう料理するか、がこの単元のほぼ全部や
順番にいくで

@9 古参ニキ
【①全体を見る】
ゴールは $\overrightarrow{OP}$ を $\vec{a}$ と $\vec{b}$ で書くこと
平面上のベクトルは、$\vec{0}$ でなく平行でもない2本 $\vec{a}, \vec{b}$ を使えば
どれも [[$x\vec{a}+y\vec{b}$ の形でただ1通りに表せる]]
つまり「$\vec{a}$ の係数」と「$\vec{b}$ の係数」の2つの数を決めればゴール

@10 名無し
座標の $(x,\ y)$ みたいなもんか

@11 古参ニキ
>>10
それな。$\vec{a}, \vec{b}$ が「斜めの座標軸」で、係数が座標や
$\vec{a}\neq\vec{0}$, $\vec{b}\neq\vec{0}$ で平行でないとき、$\vec{a}$ と $\vec{b}$ は [[一次独立]] っていう
この条件が後で効いてくるから覚えといて

@12 古参ニキ
【②知識の利用】
使える道具は内分点の公式
線分 XY を $m:n$ に内分する点 Z は
$$\overrightarrow{OZ}=\frac{n\overrightarrow{OX}+m\overrightarrow{OY}}{m+n}$$
数IIの座標の内分点と同じ形や

@13 イッチ
>>12
C は OA を $2:1$ やから $\overrightarrow{OC}=\frac{2}{3}\vec{a}$
D は中点やから $\overrightarrow{OD}=\frac{1}{2}\vec{b}$
ここまではええけど、P は比が書いてないから公式使えんやん

@14 古参ニキ
>>13
そこで【③部分を見る】
P を「AD 上の点」として見るのと「BC 上の点」として見るのに分ける
比がわからんなら [[わからん比を文字でおく]]
AP:PD $=s:(1-s)$ とおくと
$$\overrightarrow{OP}=(1-s)\vec{a}+s\overrightarrow{OD}$$

@15 名無し
>>14
今の $(1-s)$ ってどっから出てきたん

@16 古参ニキ
>>15
内分点の公式で $m=s$, $n=1-s$ にしただけや。分母は $s+(1-s)=1$ で消える
「A の係数が $1-s$、D の係数が $s$」で、**係数の和が 1** になるのがポイント
P が A に近いほど A の係数が大きい、ってイメージや

@17 イッチ
ほな $\overrightarrow{OD}=\frac{1}{2}\vec{b}$ を入れて
$$\overrightarrow{OP}=(1-s)\vec{a}+\frac{s}{2}\vec{b}$$
……で、$s$ がわからんのやが

@18 古参ニキ
>>17
せや、直線1本だけやと P は決まらん
P は「BC 上の点」でもあるやろ。もう1回同じことをやるんや

@19 イッチ
ほな BC も同じように BP:PC $=s:(1-s)$ とおいて
$$\overrightarrow{OP}=\frac{2}{3}s\,\vec{a}+(1-s)\vec{b}$$
>>17 と係数を比べると
$\vec{a}$：$1-s=\frac{2}{3}s$ → $s=\frac{3}{5}$
$\vec{b}$：$\frac{s}{2}=1-s$ → $s=\frac{2}{3}$

@20 イッチ
……$s$ が2個出てきたンゴ
$\frac{3}{5}$ と $\frac{2}{3}$ で合わんから、AD と BC は交わらない？

@21 名無し
>>20
図で交わってるのに交わらないは草

@22 名無し
>>19
BC 側でも $s$ 使ってるやん
AP:PD と BP:PC が同じ比になる理由どこにあるんや

@23 イッチ
>>22
あっ

@24 古参ニキ
>>22
正論パンチや
AP:PD と BP:PC は別の比。たまたま一致する保証はどこにもない
別の量には [[別の文字]] をおく。BC 側は $t$ にせなあかん

@25 古参ニキ
なんでこう間違えるかっていうと
「内分の比は $s$ でおく」って文字ごと丸暗記してるからや
文字は飾りの名前やなくて「未知数」。未知数が2個なら文字も2個
で、式も2本（$\vec{a}$ の係数と $\vec{b}$ の係数）作れるから、ちゃんと決まる

@26 イッチ
ほなやり直す。BP:PC $=t:(1-t)$ とおいて
$$\overrightarrow{OP}=(1-t)\vec{b}+t\overrightarrow{OC}=\frac{2}{3}t\,\vec{a}+(1-t)\vec{b}$$

@27 古参ニキ
>>26
そう。これで P を2通りに表せた
ここで >>11 が効いてくる
$\vec{a}, \vec{b}$ は一次独立やから、表し方はただ1通り
→ 2つの式の [[係数どうしが等しい]] って言えるんや

@28 名無し
だから「平行でない」をわざわざ確認するんか

@29 古参ニキ
>>28
それな。答案にも「$\vec{a}, \vec{b}$ は一次独立であるから」って一言書く
平行やったら $\vec{a}=2\vec{b}$ みたいに混ざってしまって、係数を比べても意味ないからな

@30 イッチ
>>17 と >>26 で係数比較
$\vec{a}$ の係数：$1-s=\frac{2}{3}t$
$\vec{b}$ の係数：$\frac{s}{2}=1-t$
2本目から $s=2-2t$

@31 イッチ
1本目に入れて
$1-(2-2t)=\frac{2}{3}t$
$2t-1=\frac{2}{3}t$
$\frac{4}{3}t=1$ やから $t=\frac{3}{4}$、$s=2-\frac{3}{2}=\frac{1}{2}$

@32 イッチ
$s=\frac{1}{2}$ を >>17 に入れて
$$\overrightarrow{OP}=\frac{1}{2}\vec{a}+\frac{1}{4}\vec{b}$$
これ答え？

@33 古参ニキ
>>32
正解。検算もしとこ。$t=\frac{3}{4}$ を >>26 に入れると
$\frac{2}{3}\cdot\frac{3}{4}=\frac{1}{2}$、$1-\frac{3}{4}=\frac{1}{4}$ で一致
ついでに $s=\frac{1}{2}$ ってことは、P は AD の中点やな

@34 名無し
最後ただの連立方程式やんけ

@35 古参ニキ
>>34
そう、まさにそれ
交点のベクトルは [[2通りに表して係数比較 → 連立方程式]] に還元できる
図形の問題が、中2の連立方程式に強制送還されたわけや

:::point 交点の位置ベクトル
1. 内分点の公式で、比がわかる点（C, D）を $\vec{a}, \vec{b}$ で表す
2. 交点を「直線①上の点」「直線②上の点」の2通りで表す。**比の文字は別々（$s$ と $t$）**
3. $\vec{a}, \vec{b}$ は一次独立 → 係数比較 → 連立方程式
:::

@36 イッチ
続きで長さも聞かれとる
$|\vec{a}|=2$, $|\vec{b}|=4$, $\angle\mathrm{AOB}=60^\circ$ のとき $|\overrightarrow{OP}|$ を求めよ
$\frac{1}{2}\times 2+\frac{1}{4}\times 4=2$ で終わりやろ

@37 名無し
>>36
ベクトルの長さはそのまま足せんぞ
向きがちゃうんやから、三角形の2辺の和を答えてるのと同じや

@38 古参ニキ
>>37
せや。前スレの [[内積]] の出番や。長さは2乗して内積で計算する
定義は $\vec{a}\cdot\vec{b}=|\vec{a}||\vec{b}|\cos\theta$（$\theta$ は2本のなす角）
で、自分自身との内積は $\theta=0^\circ$ やから $\vec{p}\cdot\vec{p}=|\vec{p}|^2$ になる

@39 古参ニキ
内積は普通の文字式と同じように展開できる
$$\left|\tfrac{1}{2}\vec{a}+\tfrac{1}{4}\vec{b}\right|^2=\tfrac{1}{4}|\vec{a}|^2+\tfrac{1}{4}\vec{a}\cdot\vec{b}+\tfrac{1}{16}|\vec{b}|^2$$
$(x+y)^2$ の展開への還元や

@40 名無し
>>39
真ん中の $\frac{1}{4}$ どっから

@41 古参ニキ
>>40
$2\times\frac{1}{2}\times\frac{1}{4}=\frac{1}{4}$。$(x+y)^2=x^2+2xy+y^2$ の $2xy$ のとこや

@42 イッチ
$\vec{a}\cdot\vec{b}=2\cdot 4\cdot\cos 60^\circ=4$ やから
$\frac{1}{4}\cdot 4+\frac{1}{4}\cdot 4+\frac{1}{16}\cdot 16=1+1+1=3$
$|\overrightarrow{OP}|=\sqrt{3}$
>>36 の 2 と全然ちゃうやん

@43 古参ニキ
>>42
正解。長さは「2乗して、内積で展開」がテンプレや
ベクトルの長さを、数Iの展開と三角比に還元してるだけやで

@44 イッチ
ほな自分で1問やらせてや
△OAB で OA を $1:2$ に内分する点 C、OB の中点 D、AD と BC の交点 P
4ステップ言いながらやる

@45 名無し
ksk

@46 イッチ
【①全体を見る】
ゴールは $\overrightarrow{OP}=(\ \ )\vec{a}+(\ \ )\vec{b}$ の係数2つ。$\vec{a}, \vec{b}$ は一次独立
【②知識の利用】
内分点の公式で $\overrightarrow{OC}=\frac{1}{3}\vec{a}$、$\overrightarrow{OD}=\frac{1}{2}\vec{b}$

@47 イッチ
【③部分を見る】
P を2通りに分けて見る。文字は別々や
AP:PD $=s:(1-s)$ → $\overrightarrow{OP}=(1-s)\vec{a}+\frac{s}{2}\vec{b}$
BP:PC $=t:(1-t)$ → $\overrightarrow{OP}=\frac{t}{3}\vec{a}+(1-t)\vec{b}$

@48 イッチ
係数比較して $1-s=\frac{t}{3}$、$\frac{s}{2}=1-t$
2本目から $s=2-2t$、1本目に入れて $2t-1=\frac{t}{3}$
$t=\frac{3}{5}$、$s=\frac{4}{5}$
$$\overrightarrow{OP}=\frac{1}{5}\vec{a}+\frac{2}{5}\vec{b}$$

@49 名無し
おお、検算は？

@50 イッチ
>>49
$t=\frac{3}{5}$ で BC 側：$\frac{1}{3}\cdot\frac{3}{5}=\frac{1}{5}$、$1-\frac{3}{5}=\frac{2}{5}$。一致や
え、ワイ天才では？

@51 古参ニキ
>>50
完璧や。$s$ と $t$ を分けた時点で勝ちやったな
ちなみに空間ベクトルでも発想は全く同じ
同じ平面上にない3本 $\vec{a}, \vec{b}, \vec{c}$ で、空間のベクトルは全部ただ1通りに表せる
係数比較の式が3本になるだけや

@52 名無し
次元が増えても「基準のベクトルで書いて係数比較」は変わらんのか

@53 古参ニキ
>>52
それな。空間でよく出るのは「点 P が平面 ABC 上にある」条件
$\overrightarrow{OP}=x\vec{a}+y\vec{b}+z\vec{c}$ と書けたら [[$x+y+z=1$]]
>>16 の「係数の和が 1」の3本版や。練習問題の発展でやってみ

@54 イッチ
今回 ④ 使わんかったけど、ええの？

@55 古参ニキ
>>54
③までで全部解けたなら、それが理想や
④は「始点を O 以外に取り直す」「メネラウスの定理で先に比を出す」みたいな近道
知ってたら速いけど、知らんでも③までで必ず着く

@56 古参ニキ
ほなまとめるで

:::point このスレのテンプレ
1. 【①全体を見る】ゴールは「基準のベクトル $\vec{a}, \vec{b}$ の係数」を決めること。$\vec{a}, \vec{b}$ が [[一次独立]] か確認
2. 【②知識の利用】内分点の公式／内積 $\vec{a}\cdot\vec{b}=|\vec{a}||\vec{b}|\cos\theta$
3. 【③部分を見る】交点は「どの直線上にあるか」で分けて **2通り** に表す（比の文字は別々）→ 係数比較
4. 【④工夫する】始点の取り直し、メネラウスの定理で近道

長さを聞かれたら「2乗して内積で展開」。空間でも基準が3本になるだけ。
:::

@57 イッチ
めんどくさいけど
「わからん比は文字にして、2通りから挟み撃ち」はわかったわ

@58 名無し
>>57
名スレ

@59 名無し
定規ベクトル民、卒業おめ

## 練習問題

:::exercise 基本
$|\vec{a}|=3$, $|\vec{b}|=2$, $|\vec{a}-\vec{b}|=\sqrt{7}$ のとき、内積 $\vec{a}\cdot\vec{b}$ と、$\vec{a}$ と $\vec{b}$ のなす角 $\theta$（$0^\circ\leqq\theta\leqq 180^\circ$）を求めよ。
:::

:::answer
【①全体を見る】ゴールは内積と角。角は内積の定義 $\vec{a}\cdot\vec{b}=|\vec{a}||\vec{b}|\cos\theta$ から出す。
【②知識の利用】長さの条件は「2乗して内積で展開」。
$$|\vec{a}-\vec{b}|^2=|\vec{a}|^2-2\vec{a}\cdot\vec{b}+|\vec{b}|^2$$
【③部分を見る】わかっている値を代入する。
$$7=9-2\vec{a}\cdot\vec{b}+4$$
よって $\vec{a}\cdot\vec{b}=3$。
$$\cos\theta=\frac{3}{3\cdot 2}=\frac{1}{2}$$
答え：[[$\vec{a}\cdot\vec{b}=3$, $\theta=60^\circ$]]
:::

:::exercise 標準
△OAB で、辺 OA を $3:1$ に内分する点を C、辺 OB を $2:3$ に内分する点を D とし、線分 AD と BC の交点を P とする。$\overrightarrow{OA}=\vec{a}$, $\overrightarrow{OB}=\vec{b}$ として、$\overrightarrow{OP}$ を $\vec{a}, \vec{b}$ で表せ。また AP:PD を求めよ。
:::

:::answer
【①全体を見る】ゴールは $\vec{a}, \vec{b}$ の係数2つ。$\vec{a}, \vec{b}$ は一次独立。
【②知識の利用】内分点の公式から $\overrightarrow{OC}=\frac{3}{4}\vec{a}$、$\overrightarrow{OD}=\frac{2}{5}\vec{b}$。
【③部分を見る】P を2通りに表す。AP:PD $=s:(1-s)$、BP:PC $=t:(1-t)$ とおくと
$$\overrightarrow{OP}=(1-s)\vec{a}+\frac{2}{5}s\,\vec{b}=\frac{3}{4}t\,\vec{a}+(1-t)\vec{b}$$
$\vec{a}, \vec{b}$ は一次独立だから係数を比較して
$$1-s=\frac{3}{4}t,\quad \frac{2}{5}s=1-t$$
2式目から $t=1-\frac{2}{5}s$。1式目に代入して $1-s=\frac{3}{4}-\frac{3}{10}s$、よって $\frac{7}{10}s=\frac{1}{4}$、$s=\frac{5}{14}$（$t=\frac{6}{7}$）。

答え：[[$\overrightarrow{OP}=\frac{9}{14}\vec{a}+\frac{1}{7}\vec{b}$]]、AP:PD $=s:(1-s)=$ [[$5:9$]]

検算：$\frac{3}{4}t=\frac{3}{4}\cdot\frac{6}{7}=\frac{9}{14}$、$1-t=\frac{1}{7}$ で一致。
:::

:::exercise 発展
四面体 OABC において、$\overrightarrow{OA}=\vec{a}$, $\overrightarrow{OB}=\vec{b}$, $\overrightarrow{OC}=\vec{c}$ とする。辺 OA の中点を D、辺 OB を $2:1$ に内分する点を E、辺 OC を $1:3$ に内分する点を F とし、△ABC の重心を G とする。直線 OG と平面 DEF の交点を P とするとき、$\overrightarrow{OP}$ を $\vec{a}, \vec{b}, \vec{c}$ で表せ。
:::

:::answer
【①全体を見る】空間なので基準は一次独立な3本 $\vec{a}, \vec{b}, \vec{c}$。P は「直線 OG 上」かつ「平面 DEF 上」。2つの条件で P を決める。
【②知識の利用】重心は $\overrightarrow{OG}=\frac{1}{3}(\vec{a}+\vec{b}+\vec{c})$。点 P が平面 DEF 上 ⇔ $\overrightarrow{OP}=x\overrightarrow{OD}+y\overrightarrow{OE}+z\overrightarrow{OF}$ かつ $x+y+z=1$。
【③部分を見る】まず直線 OG 上だから $\overrightarrow{OP}=k\overrightarrow{OG}=\frac{k}{3}(\vec{a}+\vec{b}+\vec{c})$。
次に $\overrightarrow{OD}=\frac{1}{2}\vec{a}$, $\overrightarrow{OE}=\frac{2}{3}\vec{b}$, $\overrightarrow{OF}=\frac{1}{4}\vec{c}$ より、$\vec{a}=2\overrightarrow{OD}$, $\vec{b}=\frac{3}{2}\overrightarrow{OE}$, $\vec{c}=4\overrightarrow{OF}$。代入して
$$\overrightarrow{OP}=\frac{2k}{3}\overrightarrow{OD}+\frac{k}{2}\overrightarrow{OE}+\frac{4k}{3}\overrightarrow{OF}$$
$\overrightarrow{OD}, \overrightarrow{OE}, \overrightarrow{OF}$ は同じ平面上にないので、係数の和が 1：
$$\frac{2k}{3}+\frac{k}{2}+\frac{4k}{3}=\frac{5}{2}k=1$$
よって $k=\frac{2}{5}$。

答え：[[$\overrightarrow{OP}=\frac{2}{15}(\vec{a}+\vec{b}+\vec{c})$]]

ポイント：「直線上」は $k$ 倍、「平面上」は係数の和が 1。平面のときの「2通りに表して係数比較」と同じく、条件を1つずつ式にしているだけ。
:::

:::check ③までやり切れチェック
- ゴールを「基準のベクトルの係数を決めること」と言えたか
- 基準のベクトルが一次独立（平面は2本・空間は3本）であることを確認したか
- 交点を「どの直線（平面）上にあるか」で分けて、2通りに表したか
- わからない比に、それぞれ別の文字をおいたか
- 長さは「2乗して内積で展開」したか
:::
