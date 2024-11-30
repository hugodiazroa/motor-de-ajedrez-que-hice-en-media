from math import *
from random import *
import md5
###################################################### Definitions

NAME = "Hugo 1.0"
CUADRADOS = 120
DURACIONMAXIMA = 2048
VACIO, Pb, Cb, Ab, Tb, Db, Rb, Pn, Cn, An, Tn, Dn, Rn = xrange(13)
NOMBRESPIEZAS = ["..", "Pb", "Cb", "Ab", "Tb", "Db", "Rb", "Pn", "Cn", "An", "Tn", "Dn", "Rn"]
Y_A, Y_B, Y_C, Y_D, Y_E, Y_F, Y_G, Y_H, Y_NINGUNA = xrange(9)
X_1, X_2, X_3, X_4, X_5, X_6, X_7, X_8, X_NINGUNA = xrange(9)
BLANCO, NEGRO, AMBOS = xrange(3)
NOMBRELADO = ["BLANCO", "NEGRO", "AMBOS"]
A1, B1, C1, D1, E1, F1, G1, H1 = xrange (21, 29)
A2, B2, C2, D2, E2, F2, G2, H2 = xrange (31, 39)
A3, B3, C3, D3, E3, F3, G3, H3 = xrange (41, 49)
A4, B4, C4, D4, E4, F4, G4, H4 = xrange (51, 59)
A5, B5, C5, D5, E5, F5, G5, H5 = xrange (61, 69)
A6, B6, C6, D6, E6, F6, G6, H6 = xrange (71, 79)
A7, B7, C7, D7, E7, F7, G7, H7 = xrange (81, 89)
A8, B8, C8, D8, E8, F8, G8, H8, SIN_CUAD, OFFBOARD = xrange (91, 101)

NOMBRESCUADRADOS =	[]
for i in range(21): NOMBRESCUADRADOS.append(0)
laux1=["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1",0,0,"A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2",0,0,"A3", "B3", "C3", "D3", "E3", "F3", "G3", "H3",0,0,"A4", "B4", "C4", "D4", "E4", "F4", "G4", "H4",0,0,"A5", "B5", "C5", "D5", "E5", "F5", "G5", "H5",0,0,"A6", "B6", "C6", "D6", "E6", "F6", "G6", "H6",0,0,"A7", "B7", "C7", "D7", "E7", "F7", "G7", "H7",0,0,"A8", "B8", "C8", "D8", "E8", "F8", "G8", "H8", "SIN_CUAD", "OFFBOARD"]
for i in laux1: NOMBRESCUADRADOS.append(i)


FEN_INICIAL = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
FEN_1 = "rnbqkbnr/pppppppp/8/8/4P3/8/PPPP1PPP/RNBQKBNR b KQkq e3 0 1"
FEN_2 = "rnbqkbnr/pp1ppppp/8/2p5/4P3/8/PPPP1PPP/RNBQKBNR w KQkq c6 0 2"
FEN_3 = "rnbqkbnr/pp1ppppp/8/2p5/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2"
FEN_D = "K6k/8/8/8/4Q3/8/8/8 w - - 0 1"
FEN_T = "K6k/8/8/8/5r2/8/8/8 b - - 0 1"
FEN_C = "K6k/8/8/8/4N3/8/8/8 w - - 0 1"
FEN_A = "K6k/8/8/8/4b3/8/8/8 w - - 0 1"
FEN_Pb = "rnbqkb1r/pp1p1pPp/8/2p1pP2/1P1P4/3P3P/P1P1P3/RNBQKBNR w KQkq - 1 2"
FEN_Pn = "rnbqkbnr/p1p1p3/3p3p/1p1p4/2P1Pp2/8/PP1P1PpP/RNBQKB1R b KQkq - 1 2"
FEN_Caballo = "5k2/1n6/4n3/6N1/8/3N4/8/5K2 w - - 0 1"
FEN_Torres = "6k1/8/5r2/8/1nR5/5N2/8/6K1 b - - 0 1"
FEN_Damas = "6k1/8/4nq2/8/1nQ5/5N2/1N6/6K1 b - - 0 1"
FEN_Alfiles = "6k1/1b6/4n3/8/8/1n4B1/1B3N2/2b3K1 w - - 0 1"
FEN_Enroque_1 = "r3k2r/8/8/8/8/8/8/R3K2R b KQkq - 0 1"
FEN_Enroque_2 = "3rk2r/8/8/8/8/8/6p1/R3K2R w KQq - 0 1"


BOO=1
BOOO=2
NOO=4
NOOO=8

bitTable = [63, 30, 3, 32, 25, 41, 22, 33, 15, 50, 42, 13, 11, 53, 19, 34, 61, 29, 2, 51, 21, 43, 45, 10, 18, 47, 1, 54, 9, 57, 0, 35, 62, 31, 40, 4, 49, 5, 52, 26, 60, 6, 23, 44, 46, 27, 56, 16, 7, 39, 48, 24, 59, 14, 12, 55, 38, 28, 58, 20, 37, 17, 36, 8]

posicion = { 
"piezas" : [0 for i in range(CUADRADOS)],
"peones" : [0 for i in range(3)] , 
"ReyCuadrado" : [0 for i in  range(2)], 
"enroquePermitido" : 0 , 
"ladoMov" : 0, 
"alPaso" : 0, 
"cincuentaM" : 0, 
"jugada" : 0, 
"mediaJugada" : 0, 
"posLlave" : 0, 
"pieNum" : [0 for i in  range(13)], 
"piezasTotal" : [0 for i in  range(2)], 
"piezasMay" : [0 for i in  range(2)], 
"piezasMen" : [0 for i in  range(2)], 
"material" : [0 for i in  range(2)], 
"piezasLista" : [[0 for i in  range(10)] for i in  range(13)]}


piezaEsPieza = [0,0,1,1,1,1,1,0,1,1,1,1,1]
piezaEsMayor = [0,0,0,0,1,1,1,0,0,0,1,1,1]
piezaEsMenor = [0,0,1,1,0,0,0,0,1,1,0,0,0]
piezaEsCaballo = [0,0,1,0,0,0,0,0,1,0,0,0,0]
piezaEsDamaAlfil = [0,0,0,1,0,1,0,0,0,1,0,1,0]
piezaEsDamaTorre = [0,0,0,0,1,1,0,0,0,0,1,1,0]
piezaEsrey = [0,0,0,0,0,0,1,0,0,0,0,0,1]
piezaEsPeon = [0,1,0,0,0,0,0,1,0,0,0,0,0]
piezaValor = [0,100,350,350,550,1000,29052000,100,350,350,550,1000,29052000]
piezaColor = [AMBOS,BLANCO,BLANCO,BLANCO,BLANCO,BLANCO,BLANCO,NEGRO,NEGRO,NEGRO,NEGRO,NEGRO,NEGRO]
piezaDesplaza = [0,0,0,1,1,1,0,0,0,1,1,1,0]

dirCaballo = [-21,-19,-12,-8,8,12,19,21]
dirTorre = [-10,-1,1,10]
dirAlfil = [-11,-9,9,11]
dirRey = [-11,-10,-9,-1,1,9,10,11]
direccionPiezas = [[],
[],dirCaballo,dirAlfil,dirTorre,dirRey,dirRey,
[],dirCaballo,dirAlfil,dirTorre,dirRey,dirRey]

permisosEnroque = [15 for i in range(120)]
permisosEnroque[A1] = 13 # 1101
permisosEnroque[E1] = 12 # 1100
permisosEnroque[H1] = 14 # 1110
permisosEnroque[A8] = 7  # 0111
permisosEnroque[E8] = 3  # 0011
permisosEnroque[H8] = 11 # 1011

debugg=0

S_UNDO = {"llave" : 0,"movida":0,"alPaso": 0,"cincuentaM": 0,"permisosEnroque": 0}

T_UNDO = (0,0,0,0,0)

S_HISTORIA = {"historia" : []}

movidas = { 
"listaMovidas" : [],
"movida" : 0,
"puntuacion" : 0 }


"""
0000 0000 0000 0000 0000 0000 0000 -> movida
0000 0000 0000 0000 0000 0111 1111 -> cuadrado de donde parte la movida
0000 0000 0000 0011 1111 1000 0000 -> cuadrado donde llega la movida
0000 0000 0011 1100 0000 0000 0000 -> pieza capturada
0000 0000 0100 0000 0000 0000 0000 -> fue una captura al paso
0000 0000 1000 0000 0000 0000 0000 -> fue una primera movida de peon
0000 1111 0000 0000 0000 0000 0000 -> pieza promovida
0001 0000 0000 0000 0000 0000 0000 -> fue un enroque


"""


#################### GLOBALS

C120aC64 = [OFFBOARD for variable in  xrange(CUADRADOS)]
C64aC120 = [0 for variable in  xrange(64)]
mascaraPoner = [0 for variable in  xrange(64)]
mascaraLimpiar = [0 for variable in  xrange(64)]
xTablero = [OFFBOARD for variable in  xrange(CUADRADOS)]
yTablero = [OFFBOARD for variable in  xrange(CUADRADOS)]



################### FUNCTIONS

def FCaC(x,y): return ((21+(x))+((y)*10))

for y in xrange(8):
	for x in xrange(8):
		"""
		1 1 1 1 1 1 1 1
		2 2 2 2 2 2 2 2 
		3 3 3 3 3 3 3 3 
		4 4 4 4 4 4 4 4 
		5 5 5 5 5 5 5 5
		6 6 6 6 6 6 6 6
		7 7 7 7 7 7 7 7
		8 8 8 8 8 8 8 8
		"""
		xTablero[FCaC(x,y)] = y+1
		"""
		1 2 3 4 5 6 7 8
		1 2 3 4 5 6 7 8
		1 2 3 4 5 6 7 8
		1 2 3 4 5 6 7 8
		1 2 3 4 5 6 7 8
		1 2 3 4 5 6 7 8
		1 2 3 4 5 6 7 8
		1 2 3 4 5 6 7 8		
		"""
		yTablero[FCaC(x,y)] = x+1

def InitC120aC64():
	global C120aC64
	global C64aC120
	indice=0
	Y=Y_A
	X=X_1
	C=A1
	C64=0

	for indice in  xrange(120): C120aC64[indice]=65
	for indice in  xrange(64): C64aC120[indice]=120

	for X in  xrange(X_8+1):
		for Y in  xrange(Y_H+1):
			C=FCaC(Y,X)
			C64aC120[C64]=C
			C120aC64[C]=C64
			C64+=1

def C64(C120): return C120aC64[C120]
def C120(C64): return C64aC120[C64]
def esCab(p): return piezaEsCaballo[p]
def esAD(p): return piezaEsDamaAlfil[p]
def esTD(p): return piezaEsDamaTorre[p]
def esRey(p): return piezaEsrey[p]

def DESDEC(movida): return movida%(2**7)
def HACIAC(movida): return (movida//(2**7))%(2**7)
def CAPTURA(movida): return (movida//(2**14))%(2**4)
def PROMOCION(movida): return (movida//(2**20))%(2**4)
def PROMOVIDA(pieza): return pieza*(2**20)
def MOVIDA(desde,hacia,captura=0,promocion=0,flag=0): return (desde + hacia*(2**7) + captura*(2**14) + promocion*(2**20)) + flag
def CUADRADOOFFBOARD(cuadrado): return (piezas[cuadrado]==OFFBOARD)

def cuadradoValido(cuadrado): return not(posicion["piezas"][cuadrado]==OFFBOARD)
def ladoValido(lado): return (lado==BLANCO or lado==NEGRO)
def xyValido(xy): return (xy>=0 and xy<=7)
def piezaValidaVacio(pieza): return  (pieza>=VACIO and pieza<=Rn)
def piezaValida(pieza): return  (pieza>=Pb and pieza<=Rn)

FLAG_ALPASO = 0x40000
FLAG_INICIOPEON = 0x80000
FLAG_ENROQUE = 0x1000000
FLAG_CAPTURA = 0x7C000
FLAG_PROMOCION = 0xF00000

def strCuadrado(cuadrado): return NOMBRESCUADRADOS[cuadrado]

def strMovida(movida):
	s = ""
	s += str(NOMBRESCUADRADOS[DESDEC(movida)])
	s += str(NOMBRESCUADRADOS[HACIAC(movida)])
	if PROMOCION(movida): s += NOMBRESPIEZAS[PROMOCION(movida)]
	return s

def InitMascaras():
	global mascaraPoner
	global mascaraLimpiar
	for i in xrange(len(mascaraPoner)): mascaraPoner[i] = 2**i
	for i in xrange(len(mascaraLimpiar)): mascaraLimpiar[i] = 2**64 - 1 - mascaraPoner[i]

InitC120aC64()
InitMascaras()

def LIMPIARBIT(tb,c64): 
	global mascaraLimpiar
	return (tb & mascaraLimpiar[c64])
def PONERBIT(tb,c64): 
	global mascaraPoner
	return tb | mascaraPoner[c64]

def imprimirTaberoBit(tb):

	for Y in  xrange(7,-1,-1):
		for X in  xrange(0,8):
			c = FCaC(X,Y)
			c64 = C64(c)
			if c64==0: 
				if tb%2: print "x",
				else: print "_",
			elif tb//(2**c64)%2: print "x", 
			else: print "_",
		print 
	print 

def POP(tb):
	for i in  xrange(64): 
		if tb//(2**i)%2: return i,tb^2**(i)
	return 0,tb
#returns (position of the pop, the poped b)

def CNT(tb): 
	c=0
	for i in  xrange(64): 
		if tb//(2**i)%2: c+=1
	return c



def generarPosLlave(): return md5.new(str(posicion["piezas"])+str(posicion["enroquePermitido"])+str(posicion["ladoMov"])).hexdigest()

def resetTablero():
	global posicion
	global movidas

	# print "resetTablero se gatilla!!!"

	for i in  xrange(120): 
		posicion["piezas"][i] = OFFBOARD
	for i in xrange(64):
		posicion["piezas"][C120(i)] = 0
	for i in  xrange(2): 
		posicion["material"][i] = 0
		posicion["piezasMen"][i] = 0
		posicion["piezasMay"][i] = 0
		posicion["piezasTotal"][i] = 0
	for i in xrange(3): posicion["peones"][i] = 0
	# print "peones limpiados @ 263"
	for i in xrange(13): posicion["pieNum"][i] = 0
	posicion["ReyCuadrado"][BLANCO] = posicion["ReyCuadrado"][NEGRO] = SIN_CUAD
	posicion["ladoMov"] = AMBOS
	posicion["alPaso"] = SIN_CUAD
	posicion["cincuentaM"] = 0
	posicion["jugada"] = 0
	posicion["mediaJugada"] = 0
	posicion["enroquePermitido"] = 0
	posicion["posLlave"] = 0

	movidas["listaMovidas"] = []

def actualizarListasMaterial():
	global posicion
	
	c=0

	for i in posicion["piezas"]:
		if i in range(1,13):
			color = piezaColor[i]
			if piezaEsMenor[i]: posicion["piezasMen"][color]+=1
			if piezaEsMayor[i]: posicion["piezasMay"][color]+=1
			if piezaEsPieza[i]: posicion["piezasTotal"][color]+=1
			posicion["material"][color]+=piezaValor[i]

			posicion["piezasLista"][i][posicion["pieNum"][i]] = c
			posicion["pieNum"][i]+=1 
			# print piezas,"\n",i,Pb,c,C64(c),mascaraPoner,"\n"
			if esRey(i): posicion["ReyCuadrado"][color] = c
			if i==Pb:
				posicion["peones"][BLANCO] = PONERBIT(posicion["peones"][BLANCO],C64(c))
				posicion["peones"][AMBOS] = PONERBIT(posicion["peones"][AMBOS],C64(c))
			elif i==Pn:
				posicion["peones"][NEGRO] = PONERBIT(posicion["peones"][NEGRO],C64(c))
				posicion["peones"][AMBOS] = PONERBIT(posicion["peones"][AMBOS],C64(c))
			# print  "peones", posicion["peones"]
			# print 
		c+=1

def lectorFEN(string):

	resetTablero()
	global posicion

	tablero = string.split()[0].split("/")
	tablero = tablero[::-1]

	cx=X_1
	for i in tablero: 
		cy=Y_A
		for j in i:
			if j=="R": posicion["piezas"][FCaC(cy,cx)]=Tb
			if j=="N": posicion["piezas"][FCaC(cy,cx)]=Cb
			if j=="B": posicion["piezas"][FCaC(cy,cx)]=Ab
			if j=="Q": posicion["piezas"][FCaC(cy,cx)]=Db
			if j=="K": posicion["piezas"][FCaC(cy,cx)]=Rb
			if j=="P": posicion["piezas"][FCaC(cy,cx)]=Pb
			if j=="r": posicion["piezas"][FCaC(cy,cx)]=Tn
			if j=="n": posicion["piezas"][FCaC(cy,cx)]=Cn
			if j=="b": posicion["piezas"][FCaC(cy,cx)]=An
			if j=="q": posicion["piezas"][FCaC(cy,cx)]=Dn
			if j=="k": posicion["piezas"][FCaC(cy,cx)]=Rn
			if j=="p": posicion["piezas"][FCaC(cy,cx)]=Pn
			if j=="1": cy += 0
			if j=="2": cy += 1
			if j=="3": cy += 2
			if j=="4": cy += 3
			if j=="5": cy += 4
			if j=="6": cy += 5
			if j=="7": cy += 6
			if j=="8": cy += 7
			cy+=1
		cx+=1

	permisos = string.split()

	if permisos[1]=="w": posicion["ladoMov"] = BLANCO
	elif permisos[1]=="b": posicion["ladoMov"] = NEGRO

	enroquePermitido=0
	if "K" in permisos[2]: posicion["enroquePermitido"]+=BOO
	if "Q" in permisos[2]: posicion["enroquePermitido"]+=BOOO
	if "k" in permisos[2]: posicion["enroquePermitido"]+=NOO
	if "q" in permisos[2]: posicion["enroquePermitido"]+=NOOO

	if permisos[3] != "-": posicion["alPaso"] = eval(permisos[3].capitalize())
	else: posicion["alPaso"] = SIN_CUAD

	if debugg: posicion["posLlave"] = generarPosLlave()

	actualizarListasMaterial()

def imprimirTablero():
	global posicion

	y=Y_A
	x=X_8
	
	while True:
		if y==Y_A: print x + 1,
		print " ",
		print NOMBRESPIEZAS[posicion["piezas"][FCaC(y,x)]],
		if y==Y_H and x!=X_1: 
			print 
			y=Y_A
			x-=1
		elif y==Y_H and x==X_1: break
		else: y+=1

	print 
	print "    A    B    C    D    E    F    G    H "
	print 
	print "lado a mover: "+NOMBRELADO[posicion["ladoMov"]]
	
	string = ""

	if posicion["enroquePermitido"] == 0: pass
	if posicion["enroquePermitido"]%2==1: string += "BOO " 
	if posicion["enroquePermitido"]/2%2==1: string += "BOOO " 
	if posicion["enroquePermitido"]/4%2==1: string += "NOO " 
	if posicion["enroquePermitido"]/8%2==1: string += "NOOO " 

	print "enroques permitidos: " + string
	print "cuadrado al paso: " + NOMBRESCUADRADOS[posicion["alPaso"]]
	if debugg: print "hash de la posicion: "+ str(posicion["posLlave"]) 
	print "\n\n\n\n\n"

def checkTablero():
	if debugg:
		t_pieNum = [0 for i in  range(13)]
		t_piezasTotal = [0 for i in  range(2)]
		t_piezasMay = [0 for i in  range(2)]
		t_piezasMen = [0 for i in  range(2)]
		t_material = [0 for i in  range(2)]

		#print "@ checkTablero; posicion[\"peones\"]: ", posicion["peones"]
		t_peones = [i for i in posicion["peones"]]
		#print "@ checkTablero; posicion[\"peones\"]: ", posicion["peones"]
		#print "@ checkTablero; t_peones: ", t_peones	
		
		#check p.ieces lists
		for i in range(Pb,Rn+1):
			for j in range(posicion["pieNum"][i]):
				c120=posicion["piezasLista"][i][j]
				assert posicion["piezas"][c120]==i

		#check p.iece count 
		for i in range(64):
			c120=C120(i)
			t_pieza=posicion["piezas"][c120]
			t_pieNum[t_pieza]+=1
			color=piezaColor[t_pieza]
			# print t_pieza, piezaEsMenor
			if t_pieza != OFFBOARD and t_pieza != SIN_CUAD:
				if piezaEsMayor[t_pieza]: t_piezasMay[color] += 1
				if piezaEsMenor[t_pieza]: t_piezasMen[color] += 1
				if piezaEsPieza[t_pieza]: t_piezasTotal[color] += 1
				if color != AMBOS: t_material[color] += piezaValor[t_pieza]


		# assertions
		for i in range(Pb,Rn+1):
			assert t_pieNum[i]==posicion["pieNum"][i]

		# print posicion
		# print posicion["piezas"]
		# print "cnt: ", CNT(t_peones[BLANCO])
		# print "pieNum[pb]: ", posicion["pieNum"][Pb]
		# print "t_peones: ", t_peones
		# print "pieNum: ", posicion["pieNum"]

		assert CNT(t_peones[BLANCO])==posicion["pieNum"][Pb]
		assert CNT(t_peones[NEGRO])==posicion["pieNum"][Pn]
		assert CNT(t_peones[AMBOS])==(posicion["pieNum"][Pb]+posicion["pieNum"][Pn])
		
		#print "@ checkTablero; posicion[\"peones\"] 1.1: ", posicion["peones"]
		#print "@ checkTablero; t_peones 1.1: ", t_peones	
		while t_peones[BLANCO]:
			assert posicion["piezas"][C120(POP(t_peones[BLANCO])[0])]==Pb
			t_peones[BLANCO]=POP(t_peones[BLANCO])[1]

		while t_peones[NEGRO]:
			assert posicion["piezas"][C120(POP(t_peones[NEGRO])[0])]==Pn
			t_peones[NEGRO]=POP(t_peones[NEGRO])[1]	

		while t_peones[AMBOS]:
			boolean = posicion["piezas"][C120(POP(t_peones[AMBOS])[0])]==Pb or posicion["piezas"][C120(POP(t_peones[AMBOS])[0])]==Pn
			assert boolean
			t_peones[AMBOS]=POP(t_peones[AMBOS])[1]
		#print "@ checkTablero; posicion[\"peones\"] 1.9: ", posicion["peones"]
		#print "@ checkTablero; t_peones 1.9: ", t_peones	


		assert t_material[BLANCO]==posicion["material"][BLANCO]
		assert t_material[NEGRO]==posicion["material"][NEGRO]
		assert t_piezasMen[BLANCO]==posicion["piezasMen"][BLANCO]
		assert t_piezasMen[NEGRO]==posicion["piezasMen"][NEGRO]
		assert t_piezasMay[BLANCO]==posicion["piezasMay"][BLANCO]
		assert t_piezasMay[NEGRO]==posicion["piezasMay"][NEGRO]
		assert t_piezasTotal[BLANCO]==posicion["piezasTotal"][BLANCO]
		assert t_piezasTotal[NEGRO]==posicion["piezasTotal"][NEGRO]

		assert posicion["ladoMov"]==BLANCO or posicion["ladoMov"]==NEGRO
		assert generarPosLlave()==posicion["posLlave"]

		assert posicion["alPaso"]==SIN_CUAD or (posicion["ladoMov"]==BLANCO and xTablero[posicion["alPaso"]]==6) or (posicion["ladoMov"]==NEGRO and xTablero[posicion["alPaso"]]==3)

		assert posicion["piezas"][posicion["ReyCuadrado"][BLANCO]]==Rb
		assert posicion["piezas"][posicion["ReyCuadrado"][NEGRO]]==Rn

		# print "@ checkTablero 2; posicion[\"peones\"]: ", posicion["peones"]
		# print "t_peones 2: ", t_peones
		# print

		return True
	else: return True

def estaAtacado(cuadrado,lado):
	global posicion
	global dirCaballo
	global dirRey
	global dirAlfil
	global dirTorre
	global C64aC120

	assert ladoValido(lado)
	assert cuadradoValido(cuadrado)
	assert checkTablero()


	if lado==BLANCO and (posicion["piezas"][cuadrado-11]==Pb or posicion["piezas"][cuadrado-9]==Pb): return True
	if lado==NEGRO and (posicion["piezas"][cuadrado+11]==Pn or posicion["piezas"][cuadrado+9]==Pn): return True
	for i in dirCaballo:
		if posicion["piezas"][cuadrado+i]==OFFBOARD: pass
		elif esCab(posicion["piezas"][cuadrado+i]) and piezaColor[posicion["piezas"][cuadrado+i]]==lado: return True
	for i in dirRey:
		if posicion["piezas"][cuadrado+i]==OFFBOARD: pass	
		elif esRey(posicion["piezas"][cuadrado+i]) and piezaColor[posicion["piezas"][cuadrado+i]]==lado: return True
	for i in dirAlfil:
		c=1
		while 1:
			if not(cuadrado+(i*c) in C64aC120) or cuadrado+(i*c)==OFFBOARD: break 
			elif posicion["piezas"][cuadrado+(i*c)] != VACIO and esAD(posicion["piezas"][cuadrado+(i*c)]) and piezaColor[posicion["piezas"][cuadrado+(i*c)]]==lado: return True
			elif posicion["piezas"][cuadrado+(i*c)] != VACIO: break
			else: c+=1
	for i in dirTorre:
		c=1
		while 1:
			if not(cuadrado+(i*c) in C64aC120) or cuadrado+(i*c)==OFFBOARD: break 
			elif posicion["piezas"][cuadrado+(i*c)] != VACIO and esTD(posicion["piezas"][cuadrado+(i*c)]) and piezaColor[posicion["piezas"][cuadrado+(i*c)]]==lado: return True
			elif posicion["piezas"][cuadrado+(i*c)] != VACIO: break
			else: c+=1
	return False

def checkEstaAtacado(lado):
	l=[]
	print 
	for i in range(64):
		if estaAtacado(C120(i),lado): print "x",
		else: print "-",
		if i%8==7: print
	print

def appendMovidaSilenciosa(movida):
	global movidas
	puntuacion = 0
	movidas["listaMovidas"].append((movida,puntuacion))

def appendMovidaCaptura(movida):
	global movidas
	puntuacion = 1
	movidas["listaMovidas"].append((movida,puntuacion))

def appendMovidaAlPaso(movida):
	global movidas
	puntuacion = 0
	movidas["listaMovidas"].append((movida,puntuacion))

def appendCapturaPeonBlanco(desde,hacia,captura):
	assert (hacia-desde in [9,11]) 
	if xTablero[desde]==7: 
		appendMovidaCaptura(MOVIDA(desde,hacia,captura,Cb,0))
		appendMovidaCaptura(MOVIDA(desde,hacia,captura,Ab,0))
		appendMovidaCaptura(MOVIDA(desde,hacia,captura,Tb,0))
		appendMovidaCaptura(MOVIDA(desde,hacia,captura,Db,0))
	else:
		appendMovidaCaptura(MOVIDA(desde,hacia,captura,VACIO,0))

def appendMovidaPeonBlanco(desde,hacia,captura=VACIO):
	assert (hacia-desde in [10,20]) 
	assert (captura==VACIO)
	if xTablero[desde]==7: 
		appendMovidaSilenciosa(MOVIDA(desde,hacia,captura,Cb,0))
		appendMovidaSilenciosa(MOVIDA(desde,hacia,captura,Ab,0))
		appendMovidaSilenciosa(MOVIDA(desde,hacia,captura,Tb,0))
		appendMovidaSilenciosa(MOVIDA(desde,hacia,captura,Db,0))
	else:
		appendMovidaSilenciosa(MOVIDA(desde,hacia,captura,VACIO,0))

def appendCapturaPeonNegro(desde,hacia,captura):
	assert (hacia-desde in [-9,-11]) 
	if xTablero[desde]==2: 
		appendMovidaCaptura(MOVIDA(desde,hacia,captura,Cn,0))
		appendMovidaCaptura(MOVIDA(desde,hacia,captura,An,0))
		appendMovidaCaptura(MOVIDA(desde,hacia,captura,Tn,0))
		appendMovidaCaptura(MOVIDA(desde,hacia,captura,Dn,0))
	else:
		appendMovidaCaptura(MOVIDA(desde,hacia,captura,VACIO,0))

def appendMovidaPeonNegro(desde,hacia,captura=VACIO):
	assert (hacia-desde in [-10,-20]) 
	assert (captura==VACIO)
	if xTablero[desde]==2: 
		appendMovidaSilenciosa(MOVIDA(desde,hacia,captura,Cn,0))
		appendMovidaSilenciosa(MOVIDA(desde,hacia,captura,An,0))
		appendMovidaSilenciosa(MOVIDA(desde,hacia,captura,Tn,0))
		appendMovidaSilenciosa(MOVIDA(desde,hacia,captura,Dn,0))
	else:
		appendMovidaSilenciosa(MOVIDA(desde,hacia,captura,VACIO,0))

def appendTodasMovidas():

	global posicion
	global movidas

	assert checkTablero()
	assert ladoValido(posicion["ladoMov"])

	movidas["listaMovidas"]=[]

	if posicion["ladoMov"]==BLANCO:
		for i in range(posicion["pieNum"][Pb]):
			cuadrado = posicion["piezasLista"][Pb][i]
			assert cuadradoValido(cuadrado)
			if posicion["piezas"][cuadrado+10] == VACIO:
				appendMovidaPeonBlanco(cuadrado,cuadrado+10)
				if posicion["piezas"][cuadrado+20] == VACIO and xTablero[cuadrado]==2:
					appendMovidaSilenciosa(MOVIDA(cuadrado,cuadrado+20,VACIO,VACIO,FLAG_INICIOPEON))
			if posicion["piezas"][cuadrado+9] != OFFBOARD:
				if piezaColor[posicion["piezas"][cuadrado+9]] == NEGRO:
					appendCapturaPeonBlanco(cuadrado,cuadrado+9,posicion["piezas"][cuadrado+9])
			if posicion["piezas"][cuadrado+11] != OFFBOARD:
				if piezaColor[posicion["piezas"][cuadrado+11]] == NEGRO:
					appendCapturaPeonBlanco(cuadrado,cuadrado+11,posicion["piezas"][cuadrado+11])
			if cuadrado+9 == posicion["alPaso"]: 
				appendMovidaCaptura(MOVIDA(cuadrado,cuadrado+9,Pn,VACIO,FLAG_CAPTURA))
			if cuadrado+11 == posicion["alPaso"]: 
				appendMovidaCaptura(MOVIDA(cuadrado,cuadrado+11,Pn,VACIO,FLAG_CAPTURA))

		if posicion["enroquePermitido"]%2==1: 
			if posicion["piezas"][F1]==VACIO and posicion["piezas"][G1]==VACIO:
				if not(estaAtacado(F1,NEGRO)) and not(estaAtacado(E1,NEGRO)) and not(estaAtacado(G1,NEGRO)):
					appendMovidaSilenciosa(MOVIDA(E1,G1,VACIO,VACIO,FLAG_ENROQUE))
		if posicion["enroquePermitido"]/2%2==1: 
			if posicion["piezas"][D1]==VACIO and posicion["piezas"][C1]==VACIO and posicion["piezas"][B1]==VACIO:
				if not(estaAtacado(D1,NEGRO)) and not(estaAtacado(E1,NEGRO)) and not(estaAtacado(C1,NEGRO)):
					appendMovidaSilenciosa(MOVIDA(E1,C1,VACIO,VACIO,FLAG_ENROQUE))



	else:
		for i in range(posicion["pieNum"][Pn]):
			cuadrado = posicion["piezasLista"][Pn][i]
			assert cuadradoValido(cuadrado)
			if posicion["piezas"][cuadrado-10] == VACIO:
				appendMovidaPeonNegro(cuadrado,cuadrado-10)
				if posicion["piezas"][cuadrado-20] == VACIO and xTablero[cuadrado]==7:
					appendMovidaSilenciosa(MOVIDA(cuadrado,cuadrado-20,VACIO,VACIO,FLAG_INICIOPEON))
			if posicion["piezas"][cuadrado-9] != OFFBOARD:
				if piezaColor[posicion["piezas"][cuadrado-9]] == BLANCO:
					appendCapturaPeonNegro(cuadrado,cuadrado-9,posicion["piezas"][cuadrado-9])
			if posicion["piezas"][cuadrado-11] != OFFBOARD:
				if piezaColor[posicion["piezas"][cuadrado-11]] == BLANCO:
					appendCapturaPeonNegro(cuadrado,cuadrado-11,posicion["piezas"][cuadrado-11])
			if cuadrado-9 == posicion["alPaso"]: 
				appendMovidaCaptura(MOVIDA(cuadrado,cuadrado-9,Pb,VACIO,FLAG_CAPTURA))
			if cuadrado-11 == posicion["alPaso"]: 
				appendMovidaCaptura(MOVIDA(cuadrado,cuadrado-11,Pb,VACIO,FLAG_CAPTURA))

		if posicion["enroquePermitido"]//4%2==1: 
			if posicion["piezas"][F8]==VACIO and posicion["piezas"][G8]==VACIO:
				if not(estaAtacado(F8,BLANCO)) and not(estaAtacado(E8,BLANCO)) and not(estaAtacado(G8,BLANCO)):
					appendMovidaSilenciosa(MOVIDA(E8,G8,VACIO,VACIO,FLAG_ENROQUE))
		if posicion["enroquePermitido"]//8%2==1: 
			if posicion["piezas"][D8]==VACIO and posicion["piezas"][C8]==VACIO and posicion["piezas"][B8]==VACIO:
				if not(estaAtacado(D8,BLANCO)) and not(estaAtacado(E8,BLANCO)) and not(estaAtacado(C8,BLANCO)):
					appendMovidaSilenciosa(MOVIDA(E8,C8,VACIO,VACIO,FLAG_ENROQUE))


	indicesPiezas = (((Ab,Tb,Db),(Cb,Rb)),((An,Tn,Dn),(Cn,Rn)))
	deslizante = True

	for tipoDePieza in indicesPiezas[posicion["ladoMov"]]:
		for p in tipoDePieza:
			if deslizante:
				# print "deslizante",NOMBRESPIEZAS[p]
				for i in range(posicion["pieNum"][p]):
					cuadrado = posicion["piezasLista"][p][i]
					assert cuadradoValido(cuadrado)
					# print "hay un ",NOMBRESPIEZAS[p]," en ",NOMBRESCUADRADOS[cuadrado]
					for direccion in direccionPiezas[p]:
						seguir = True
						cuadradoObjetivo = cuadrado + direccion
						while seguir:
							contenido = posicion["piezas"][cuadradoObjetivo]
							if contenido != OFFBOARD:
								if contenido == VACIO:
									appendMovidaSilenciosa(MOVIDA(cuadrado,cuadradoObjetivo)) 
									cuadradoObjetivo += direccion
								elif piezaColor[contenido] != piezaColor[p]:
									appendMovidaCaptura(MOVIDA(cuadrado,cuadradoObjetivo,contenido))
									seguir = False
								elif piezaColor[contenido] == piezaColor[p]: seguir = False
								else: 
									print "que bobadas hay en: ", cuadrado, posicion["piezas"][cuadrado]
									assert False
							else: seguir = False
			else:
				# print "no deslizante",NOMBRESPIEZAS[p]
				for i in range(posicion["pieNum"][p]):
					cuadrado = posicion["piezasLista"][p][i]
					assert cuadradoValido(cuadrado)
					# print "hay un ",NOMBRESPIEZAS[p]," en ",NOMBRESCUADRADOS[cuadrado]
					for direccion in direccionPiezas[p]:
						cuadradoObjetivo = cuadrado + direccion
						contenido = posicion["piezas"][cuadradoObjetivo]
						if contenido != OFFBOARD:
							if contenido == VACIO:
								appendMovidaSilenciosa(MOVIDA(cuadrado,cuadradoObjetivo)) 
							elif piezaColor[contenido] != piezaColor[p]:
								appendMovidaCaptura(MOVIDA(cuadrado,cuadradoObjetivo,contenido))
							elif piezaColor[contenido] == piezaColor[p]: pass
							else: 
								print "que bobadas hay en: ", cuadrado, posicion["piezas"][cuadrado]
								assert False

		deslizante = False

# def MOVIDA(desde,hacia,captura,promocion,flag): return (desde + hacia*(2**7) + captura*(2**14) + promocion*(2**20)) + flag

def imprimirMovidas(listadetuples):
	c=0
	for i in listadetuples:
		c+=1
		print DESDEC(i[0])," + ",(HACIAC(i[0])-DESDEC(i[0]))," = ",(HACIAC(i[0]))
		print str(c) + "# movida: ", strMovida(i[0]), " puntuacion: ", (i[1])


def limpiarPieza(cuadrado):
	global posicion

	assert cuadradoValido(cuadrado)
	pieza = posicion["piezas"][cuadrado]
	assert piezaValida(pieza)

	color = piezaColor[pieza]


	posicion["piezas"][cuadrado] = VACIO
	posicion["material"][color] -= piezaValor[pieza]


	if piezaEsPieza[pieza]:
		posicion["piezasTotal"][color] -=1
		if piezaEsMayor[pieza]:
			posicion["piezasMay"][color] -=1
		elif piezaEsMenor[pieza]:
			posicion["piezasMen"][color] -=1
		else: assert 0

	else:
		posicion["peones"][color]=LIMPIARBIT(posicion["peones"][color],C120aC64[cuadrado])
		posicion["peones"][AMBOS]=LIMPIARBIT(posicion["peones"][AMBOS],C120aC64[cuadrado])

	for i in xrange(posicion["pieNum"][pieza]):
		if posicion["piezasLista"][pieza][i] == cuadrado:
			 t_pieNum = i
			 break

	for i in xrange(i,9):
		posicion["piezasLista"][pieza][i] = posicion["piezasLista"][pieza][i+1]
	posicion["piezasLista"][pieza][9] = VACIO

	posicion["pieNum"][pieza]-=1
	if debugg: posicion["posLlave"]=generarPosLlave()


def ponerPieza(cuadrado,pieza):
	global posicion

	assert cuadradoValido(cuadrado)
	assert piezaValida(pieza)
	assert posicion["piezas"][cuadrado] == VACIO

	color = piezaColor[pieza]

	posicion["piezas"][cuadrado] = pieza

	if piezaEsPieza[pieza]:
		posicion["piezasTotal"][color] +=1
		if piezaEsMayor[pieza]: posicion["piezasMay"][color] +=1
		elif piezaEsMenor[pieza]: posicion["piezasMen"][color] +=1
		else: assert 0
	else:
		posicion["peones"][color] = PONERBIT(posicion["peones"][color],C120aC64[cuadrado])
		posicion["peones"][AMBOS] = PONERBIT(posicion["peones"][AMBOS],C120aC64[cuadrado])
	
	posicion["material"][color] += piezaValor[pieza]
	posicion["piezasLista"][pieza][posicion["pieNum"][pieza]] = cuadrado
		
	if debugg: posicion["posLlave"]=generarPosLlave()
	posicion["pieNum"][pieza] +=1

def mover(desde,hacia):
	global posicion

	assert cuadradoValido(desde)
	assert cuadradoValido(hacia)

	pieza = posicion["piezas"][desde]
	color = piezaColor[pieza]

	# print NOMBRESCUADRADOS[desde],NOMBRESCUADRADOS[hacia],NOMBRESPIEZAS[pieza]
	# print NOMBRESCUADRADOS[posicion["alPaso"]]
	assert piezaValida(pieza)

	posicion["piezas"][desde] = VACIO
	posicion["piezas"][hacia] = pieza

	if not(piezaEsPieza[pieza]):
		posicion["peones"][color] = PONERBIT(posicion["peones"][color],C120aC64[hacia])
		posicion["peones"][AMBOS] = PONERBIT(posicion["peones"][AMBOS],C120aC64[hacia])
		posicion["peones"][color] = LIMPIARBIT(posicion["peones"][color],C120aC64[desde])
		posicion["peones"][AMBOS] = LIMPIARBIT(posicion["peones"][AMBOS],C120aC64[desde])

	boolean = 0

	for i in xrange(posicion["pieNum"][pieza]):
		if posicion["piezasLista"][pieza][i] == desde:
			 posicion["piezasLista"][pieza][i] = hacia
			 boolean = 1
			 break

	assert boolean
	
def hacerMovida(movida):
	global posicion
	assert checkTablero

	desde = DESDEC(movida)
	hacia = HACIAC(movida)
	lado = posicion["ladoMov"]

	assert cuadradoValido(desde)
	assert cuadradoValido(hacia)
	
	# print 
	# print 
	# print 
	# print 
	# print 
	# print 
	# print 
	# print posicion["piezas"][desde]
	
	assert piezaValida(posicion["piezas"][desde])

	if debugg: S_UNDO["llave"] = posicion["posLlave"]


	if(movida & FLAG_ALPASO):
		if lado == BLANCO: limpiarPieza(hacia-10)
		else: limpiarPieza(hacia+10)
	elif(movida & FLAG_ENROQUE):
		if hacia == C1: mover(A1,D1)
		elif hacia == C8: mover(A8,D8)
		elif hacia == G1: mover(H1,F1)
		elif hacia == G8: mover(H8,F8)
		else: assert 0

	S_UNDO["movida"] = movida
	S_UNDO["alPaso"] = posicion["alPaso"]
	S_UNDO["cincuentaM"] = posicion["cincuentaM"]
	S_UNDO["permisosEnroque"] = posicion["enroquePermitido"]
	# S_HISTORIA["historia"].append(S_UNDO)
	if debugg: S_HISTORIA["historia"].append((posicion["posLlave"],movida,posicion["alPaso"],posicion["cincuentaM"],posicion["enroquePermitido"]))
	else: S_HISTORIA["historia"].append((0,movida,posicion["alPaso"],posicion["cincuentaM"],posicion["enroquePermitido"]))


	posicion["enroquePermitido"] &= permisosEnroque[desde]
	posicion["enroquePermitido"] &= permisosEnroque[hacia]

	capturada = CAPTURA(movida)
	posicion["cincuentaM"] += 1

	if capturada:
		assert piezaValida(capturada)
		limpiarPieza(hacia)
		posicion["cincuentaM"] = 0

	posicion["jugada"] += 1
	posicion["mediaJugada"] += 1

	# print "es peon ",piezaEsPeon[posicion["piezas"][desde]]
	if piezaEsPeon[posicion["piezas"][desde]]:
		posicion["cincuentaM"] = 0
		if(movida & FLAG_INICIOPEON):
			if lado == BLANCO: 
				posicion["alPaso"] = desde+10
				assert xTablero[posicion["alPaso"]] == 3
			else: 
				posicion["alPaso"] = desde-10
				assert xTablero[posicion["alPaso"]] == 6
		else: posicion["alPaso"]=SIN_CUAD
	else: posicion["alPaso"]=SIN_CUAD

	mover(desde,hacia)

	promocion = PROMOCION(movida)

	if promocion:
		assert piezaValida(promocion) and not(piezaEsPeon[promocion])
		limpiarPieza(hacia)
		ponerPieza(hacia,promocion)

	if piezaEsrey[posicion["piezas"][hacia]]: posicion["ReyCuadrado"][lado] = hacia

	posicion["ladoMov"] ^= 1
	if debugg: posicion["posLlave"] = generarPosLlave()
	assert checkTablero()

	if estaAtacado(posicion["ReyCuadrado"][lado],posicion["ladoMov"]):
		desacerMovida()
		return False
	return True

def desacerMovida():
	global posicion
	assert checkTablero()

	posicion["mediaJugada"] -= 1
	posicion["jugada"] -= 1

	movida = S_HISTORIA["historia"][posicion["mediaJugada"]][1]
	desde = DESDEC(movida)
	hacia = HACIAC(movida)

	assert cuadradoValido(desde)
	assert cuadradoValido(hacia)

	posicion["alPaso"] = S_HISTORIA["historia"][posicion["mediaJugada"]][2]
	posicion["cincuentaM"] = S_HISTORIA["historia"][posicion["mediaJugada"]][3]
	posicion["enroquePermitido"] = S_HISTORIA["historia"][posicion["mediaJugada"]][4]

	posicion["ladoMov"] ^= 1

	if(movida & FLAG_ALPASO):
		if lado == BLANCO: ponerPieza(hacia-10,Pn)
		else: ponerPieza(hacia+10,Pb)
	elif(movida & FLAG_ENROQUE):
		if hacia == C1: mover(D1,A1)
		elif hacia == C8: mover(D8,A8)
		elif hacia == G1: mover(F1,H1)
		elif hacia == G8: mover(F8,H8)
		else: assert 0

	mover(hacia,desde)

	if piezaEsrey[posicion["piezas"][desde]]:
		posicion["ReyCuadrado"][posicion["ladoMov"]] = desde

	capturada = CAPTURA(movida)
	if capturada:
		assert piezaValida(capturada)
		ponerPieza(hacia,capturada)

	promocion = PROMOCION(movida)
	if promocion:
		assert piezaValida(promocion) and not(piezaEsPeon[promocion])
		limpiarPieza(desde)
		if piezaColor[promocion]==BLANCO: ponerPieza(desde,Pb)
		else: ponerPieza(desde,Pn)

	if debugg: posicion["posLlave"] = generarPosLlave()
	assert checkTablero()

	del S_HISTORIA["historia"][-1]

nodosPerfd = 0
def perfd(profundidad):
	global nodosPerfd
	global movidas

	# print profundidad
	if profundidad == 0:
		nodosPerfd+=1
		return

	# imprimirTablero()
	
	appendTodasMovidas()
	l=movidas["listaMovidas"]
	
	for i in l:
		if not(hacerMovida(i[0])): continue
		perfd(profundidad-1)
		desacerMovida()

	return

def estaRepetida():
	pass

def alfaBeta(profundidad):
	pass

lectorFEN(FEN_INICIAL)



while True:

	imprimirTablero()

	desdeInput=eval(raw_input("mover desde: ").capitalize())
	haciaInput=eval(raw_input("mover hacia: ").capitalize())
	promocion=eval(raw_input("promocion: "))
	if not(promocion in range(13)): promocion = 0

	if ("q" in str(desdeInput)) or ("q" in str(haciaInput)): break
	elif ("t" in str(desdeInput)) or ("t" in str(haciaInput)): 
		takemove()
		continue
	else: 
		if type(desdeInput)==int and type(haciaInput)==int:
			if (A1 <= desdeInput <= H8) and (A1 <= haciaInput <= H8):
				captura = posicion["piezas"][haciaInput]
				pieza = posicion["piezas"][desdeInput]

				movidaInput= MOVIDA(desdeInput,haciaInput,captura,promocion,flag=0)

'''
try:
	while 1:
		pass
except KeyboardInterrupt:
	pass
'''





































