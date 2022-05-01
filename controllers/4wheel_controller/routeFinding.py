import Graphs
import MapGraph
import math
from FoxQueue import Queue, PriorityQueue
from FoxStack import Stack


def calculateDistance(x1,y1,x2,y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return dist

def dataInitialize():
    dictOfNodes = {"road_299B_01":(47.6,-14.9),"room_200":(58,-16.3), "room_206":(58,-24.9),"road_299B_02":(41.8,-14.9),"road_209":(41.9,-28.2),"road_299B_03":(13.6,-14.9),"room_277":(11.8,-17.6),"room_275":(13.9,-17.6),"room_277_&_275":(12.8,-21.1),"room_262_&_277":(7.19,-25.8),
    "room_263_&_275":(22.3,-25.8),"room_275B":(25.2,-24.6),"room_275A_01":(25.2,-18.8),"room_275A_02":(29.6,-18.8),"room_264_&_273":(30.2,-25.7),"room_264":(29.9,-32.1),"room_273":(30.4,-15.3),"room_271A":(33,-15.3),"room_271":(37.3,-15.3),"room_263":(23.8,-32.2),"road_299B_04":(1.5,-14.9),
    "road_299B_05":(-14.5,-14.9),"room_207":(47.6,-12.6),"room_270_01":(39,-14.9),"room_270_02":(27.4,-14.9),"room_272":(22.1,-14.9),"room_276_01":(9.09,-14.9),"room_287":(-1.25,-14.9),"road_299B_06":(-7.18,-14.9),"room_288":(-7.18,-18.1),"room_288A":(-9.41,-18.1),"room_288B":(-4.66,-18.1),
    "room_289_01":(-7.03,-21.2),"room_289_02":(-13.4,-21.2),"room_289_03":(-0.17,-21.2),"room_289_&_260":(-3.27,-27.6),"room_260":(0.16,-30.6),"room_262":(3.55,-30.6),"road_299c_01":(1.87,-30.6),"road_299c_02":(1.52,-21.2),"road_299c_03":(1.87,-33.2),"room_210":(1.87,-35.5),"room_211":(3.8,-35.5),
    "room_212":(9.46,-35.5),"room_213":(11.8,-35.5),"room_214":(17.1,-35.5),"room_215":(19.6,-35.5),"room_216":(25.4,-35.5),"room_217":(27.5,-35.5),"room_218":(32.2,-35.5),"room_219":(34.2,-35.5),"room_220":(38.3,-35.5),"room_221_01":(40.2,-35.5),"room_221_02":(49.3,-35.5),"terrace":(58.2,-35.5),
    "room_222_01":(67.4,-35.5),"room_222_02":(76.5,-35.5),"room_223":(78.5,-35.5),"room_224":(83.6,-35.5),"room_225":(85.5,-35.5),"room_226":(90.5,-35.5),"room_227":(92.4,-35.5),"room_228":(98,-35.5),"room_229":(100,-35.5),"room_230":(107,-35.5),"room_231":(109,-35.5),"room_232":(114,-35.5),
    "room_233":(117,-35.5),"road_297B_01":(118,-31.9),"road_297B_02":(118,-29),"room_259":(120,-29),"road_297B_03":(118,-22.7),"road_297A_01":(115,-22.7),"road_297A_02":(113,-22.7),"road_255":(113,-20.9),"road_297A_03":(104,-22.7),"road_297A_04":(96,-22.7),"road_250_01":(96.4,-21.2),
    "road_250_02":(96.4,-15.7),"road_253_01":(94.9,-21.2),"road_253_02":(94.9,-15.5),"road_297A_05":(92.1,-22.7),"room_254":(92.1,-24.6),"room_254_&_256":(93.6,-25.2),"room_254":(104,-24.6),"room_254_&_258":(105,-24.9),"room_258":(115,-24.9),"road_297A_06":(91.1,-22.7),"road_205_01":(91.1,-21.4),
    "road_205_02":(91.1,-15.7),"road_297A_07":(80.3,-22.7),"room_252":(80.3,-24.8),"road_297A_08":(73.2,-22.7),"room_205_03":(73.2,-20.6),"room_208":(73.2,-24.7),"road_297B_04":(118,-21.2),"room_257":(120,-21.2),"road_297B_05":(118,-18.7),"road_297":(120,-18.7),"road_297B_06":(118,-13.7),
    "road_297A_01":(115,-13.7),"road_297A_02":(111,-13.7),"road_297A_03":(103,-13.7),"road_297A_04":(100,-13.7),"road_297A_05":(95.5,-13.7),"road_297A_06":(93,-13.7),"road_297A_07":(89.7,-13.7),"road_297A_08":(85.3,-13.7),"road_297A_09":(83.6,-13.7),"road_297A_10":(81.5,-13.7),"road_297A_11":(78.1,-13.7),
    "road_241_01":(78.7,-11.5),"road_241_02":(85,-11.5),"road_243_01":(93.4,-11.5),"road_243_02":(100,-11.5),"road_245_01":(103,-11.5),"road_245_02":(111,-11.5),"road_247":(115,-11.5),"room_240":(78.1,-15),"room_240A":(81.3,-15),"room_240B":(84.1,-15),"road_297A_12":(73.1,-13.7),"road_249":(121,-13.7),
    "road_249A":(121,-15.3),"road_249B":(124,-11.2),"road_249C":(122,-11.2),"road_249D":(119,-11.2),"road_299C_04":(1.48,-8.45),"room_278":(1.48,-5.51),"room_280_01":(5.52,-5.51),"room_280_02":(12.7,-2.61),"room_281_01":(12.7,2.06),"room_282":(12.7,7.38),"room_283_01":(12.7,9.2),"room_283_02":(4.14,10.2),
    "room_281_02":(5.91,0.57),"room_278A":(3.84,2.84),"room_285_01":(0.15,2.07),"room_284_&_285":(-0.99,3.11),"room_283_&_284":(0.05,4.1),"room_284":(-13.3,9.4),"road_299A_01":(-14.5,9.4),"road_299A_02":(-14.5,12.7),"road_298A_01":(3.83,12.7),"road_298B_01":(13.7,12.7),"road_298_02":(13.7,8.51),
    "road_298_03":(13.7,2.14),"road_298_04":(13.7,-2.54),"room_274B":(13.7,-5.23),"room_274A":(13.7,-8.83),"room_274":(13.7,-11.3),"road_299A_03":(-14.5,-5.61),"road_299A_04":(-14.5,-21.1),"road_299A_05":(14.5,-32.7),"road_299A_06":(-12,-32.7),"room_290":(-12,-30.7),"room_299":(-12,-34),"room_261":(-1.34,-33),
    "room_285_02":(-12.9,-2.21),"room_285_&_280":(-1.01,-4.02),"room_287_&_280":(-1.01,-7.71),"room_287_01":(-0.24,-8.79),"room_276_02":(3.52,-8.79),"room_287_02":(-12.9,-8.79),"room_280":(-12.9,-5.8)}

    
    listOfKeys = []
    for i in dictOfNodes.keys():
        listOfKeys.append(i)

    listOfValues = []
    for i in dictOfNodes.values():
        listOfValues.append(i)

    graph = MapGraph.MapGraph(len(listOfValues),listOfValues)
    
    x1,y1 = dictOfNodes.get("road_299A_01")
    x2,y2 = dictOfNodes.get("road_299A_02")
    graph.addEdge(133,132,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299A_01")
    x2,y2 = dictOfNodes.get("room_284")
    graph.addEdge(130,132,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_298A_01")
    x2,y2 = dictOfNodes.get("road_299A_02")
    graph.addEdge(133,134,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_298A_01")
    x2,y2 = dictOfNodes.get("room_283_02")
    graph.addEdge(124,134,calculateDistance(x1,y1,x2,y2))

    
    x1,y1 = dictOfNodes.get("road_298A_01")
    x2,y2 = dictOfNodes.get("road_299B_01")
    graph.addEdge(0,134,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_298_02")
    x2,y2 = dictOfNodes.get("road_299B_01")
    graph.addEdge(0,135,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_298_02")
    x2,y2 = dictOfNodes.get("room_283_01")
    graph.addEdge(123,135,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_298_02")
    x2,y2 = dictOfNodes.get("room_282")
    graph.addEdge(123,122,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_283_01")
    x2,y2 = dictOfNodes.get("room_283_02")
    graph.addEdge(123,124,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_284")
    x2,y2 = dictOfNodes.get("room_283_&_284")
    graph.addEdge(130,129,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_284")
    x2,y2 = dictOfNodes.get("room_284_&_285")
    graph.addEdge(130,128,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_285_01")
    x2,y2 = dictOfNodes.get("room_284_&_285")
    graph.addEdge(127,128,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_285_01")
    x2,y2 = dictOfNodes.get("room_278A")
    graph.addEdge(127,126,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_281_02")
    x2,y2 = dictOfNodes.get("room_278A")
    graph.addEdge(125,126,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_285_01")
    x2,y2 = dictOfNodes.get("room_281_02")
    graph.addEdge(127,125,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_281_01")
    x2,y2 = dictOfNodes.get("room_281_02")
    graph.addEdge(121,125,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_281_01")
    x2,y2 = dictOfNodes.get("road_298_03")
    graph.addEdge(121,136,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_298_02")
    x2,y2 = dictOfNodes.get("road_298_03")
    graph.addEdge(135,136,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_285_02")
    x2,y2 = dictOfNodes.get("room_285_01")
    graph.addEdge(127,148,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299A_01")
    x2,y2 = dictOfNodes.get("road_299A_03")
    graph.addEdge(131,141,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_285_02")
    x2,y2 = dictOfNodes.get("road_299A_03")
    graph.addEdge(148,141,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_280")
    x2,y2 = dictOfNodes.get("road_299A_03")
    graph.addEdge(155,141,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287_02")
    x2,y2 = dictOfNodes.get("road_299A_03")
    graph.addEdge(154,141,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287_02")
    x2,y2 = dictOfNodes.get("room_280")
    graph.addEdge(154,155,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_285_02")
    x2,y2 = dictOfNodes.get("room_280")
    graph.addEdge(148,155,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_285_02")
    x2,y2 = dictOfNodes.get("room_285_&_280")
    graph.addEdge(148,149,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287_&_280")
    x2,y2 = dictOfNodes.get("room_285_&_280")
    graph.addEdge(150,149,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_280")
    x2,y2 = dictOfNodes.get("room_285_&_280")
    graph.addEdge(155,149,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_280")
    x2,y2 = dictOfNodes.get("room_287_&_280")
    graph.addEdge(155,150,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287_02")
    x2,y2 = dictOfNodes.get("room_287_&_280")
    graph.addEdge(154,150,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287_01")
    x2,y2 = dictOfNodes.get("room_287_&_280")
    graph.addEdge(151,150,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287_01")
    x2,y2 = dictOfNodes.get("room_287_02")
    graph.addEdge(151,154,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287_01")
    x2,y2 = dictOfNodes.get("road_299C_04")
    graph.addEdge(151,117,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_278")
    x2,y2 = dictOfNodes.get("road_299C_04")
    graph.addEdge(118,117,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_276_02")
    x2,y2 = dictOfNodes.get("road_299C_04")
    graph.addEdge(153,117,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_276_02")
    x2,y2 = dictOfNodes.get("road_299C_04")
    graph.addEdge(153,117,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_278")
    x2,y2 = dictOfNodes.get("room_278A")
    graph.addEdge(126,118,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_278")
    x2,y2 = dictOfNodes.get("room_280_01")
    graph.addEdge(126,119,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_281_02")
    x2,y2 = dictOfNodes.get("room_281_01")
    graph.addEdge(121,125,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_298_03")
    x2,y2 = dictOfNodes.get("room_281_01")
    graph.addEdge(121,136,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_298_03")
    x2,y2 = dictOfNodes.get("road_298_02")
    graph.addEdge(135,136,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_298_03")
    x2,y2 = dictOfNodes.get("road_298_04")
    graph.addEdge(136,137,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_280_02")
    x2,y2 = dictOfNodes.get("road_298_04")
    graph.addEdge(120,137,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_280_02")
    x2,y2 = dictOfNodes.get("room_280_01")
    graph.addEdge(120,119,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_274B")
    x2,y2 = dictOfNodes.get("road_298_04")
    graph.addEdge(138,137,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_274B")
    x2,y2 = dictOfNodes.get("room_274A")
    graph.addEdge(138,139,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_274")
    x2,y2 = dictOfNodes.get("room_274A")
    graph.addEdge(140,139,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_274")
    x2,y2 = dictOfNodes.get("road_299B_03")
    graph.addEdge(140,5,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299A_03")
    x2,y2 = dictOfNodes.get("road_299B_05")
    graph.addEdge(141,21,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287_01")
    x2,y2 = dictOfNodes.get("room_287_02")
    graph.addEdge(151,154,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_04")
    x2,y2 = dictOfNodes.get("road_299C_04")
    graph.addEdge(20,117,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_276_02")
    x2,y2 = dictOfNodes.get("room_276_01")
    graph.addEdge(26,152,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_05")
    x2,y2 = dictOfNodes.get("road_299B_06")
    graph.addEdge(21,28,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287")
    x2,y2 = dictOfNodes.get("road_299B_06")
    graph.addEdge(27,28,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287")
    x2,y2 = dictOfNodes.get("road_299B_04")
    graph.addEdge(27,20,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_276_01")
    x2,y2 = dictOfNodes.get("road_299B_04")
    graph.addEdge(26,20,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_276_01")
    x2,y2 = dictOfNodes.get("road_299B_03")
    graph.addEdge(26,5,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_287_01")
    x2,y2 = dictOfNodes.get("room_287")
    graph.addEdge(27,151,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_06")
    x2,y2 = dictOfNodes.get("room_288")
    graph.addEdge(28,29,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_288A")
    x2,y2 = dictOfNodes.get("room_288")
    graph.addEdge(30,29,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_288B")
    x2,y2 = dictOfNodes.get("room_288")
    graph.addEdge(31,29,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_289_01")
    x2,y2 = dictOfNodes.get("room_288")
    graph.addEdge(29,32,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_05")
    x2,y2 = dictOfNodes.get("road_299A_04")
    graph.addEdge(21,142,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_289_02")
    x2,y2 = dictOfNodes.get("road_299A_04")
    graph.addEdge(33,142,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_289_02")
    x2,y2 = dictOfNodes.get("room_289_01")
    graph.addEdge(33,32,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_289_01")
    x2,y2 = dictOfNodes.get("room_289_03")
    graph.addEdge(34,32,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_289_01")
    x2,y2 = dictOfNodes.get("room_289_&_260")
    graph.addEdge(35,32,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_289_03")
    x2,y2 = dictOfNodes.get("room_289_&_260")
    graph.addEdge(34,35,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299A_05")
    x2,y2 = dictOfNodes.get("road_299A_04")
    graph.addEdge(143,142,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299A_05")
    x2,y2 = dictOfNodes.get("road_299A_06")
    graph.addEdge(143,144,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_299")
    x2,y2 = dictOfNodes.get("road_299A_06")
    graph.addEdge(146,144,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_290")
    x2,y2 = dictOfNodes.get("road_299A_06")
    graph.addEdge(145,144,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_261")
    x2,y2 = dictOfNodes.get("road_299A_06")
    graph.addEdge(147,144,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299c_03")
    x2,y2 = dictOfNodes.get("room_261")
    graph.addEdge(147,40,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299c_01")
    x2,y2 = dictOfNodes.get("road_299c_03")
    graph.addEdge(38,40,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299c_01")
    x2,y2 = dictOfNodes.get("room_260")
    graph.addEdge(38,36,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299c_01")
    x2,y2 = dictOfNodes.get("room_262")
    graph.addEdge(38,37,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299c_01")
    x2,y2 = dictOfNodes.get("road_299c_02")
    graph.addEdge(38,39,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_289_03")
    x2,y2 = dictOfNodes.get("road_299c_02")
    graph.addEdge(34,39,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_04")
    x2,y2 = dictOfNodes.get("road_299c_02")
    graph.addEdge(20,39,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_262")
    x2,y2 = dictOfNodes.get("room_262_&_277")
    graph.addEdge(37,9,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_277_&_275")
    x2,y2 = dictOfNodes.get("room_262_&_277")
    graph.addEdge(8,9,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_03")
    x2,y2 = dictOfNodes.get("room_277")
    graph.addEdge(5,6,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_277_&_275")
    x2,y2 = dictOfNodes.get("room_277")
    graph.addEdge(8,6,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_277_&_275")
    x2,y2 = dictOfNodes.get("room_275")
    graph.addEdge(8,7,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_03")
    x2,y2 = dictOfNodes.get("room_275")
    graph.addEdge(5,7,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_277_&_275")
    x2,y2 = dictOfNodes.get("room_263_&_275")
    graph.addEdge(8,10,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_277_&_275")
    x2,y2 = dictOfNodes.get("room_275A_01")
    graph.addEdge(8,12,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_263_&_275")
    x2,y2 = dictOfNodes.get("room_275A_01")
    graph.addEdge(10,12,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_275B")
    x2,y2 = dictOfNodes.get("room_263_&_275")
    graph.addEdge(11,10,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_275B")
    x2,y2 = dictOfNodes.get("room_275A_01")
    graph.addEdge(11,12,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_277_&_275")
    x2,y2 = dictOfNodes.get("room_275B")
    graph.addEdge(8,11,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_263_&_275")
    x2,y2 = dictOfNodes.get("room_263")
    graph.addEdge(10,19,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_275A_02")
    x2,y2 = dictOfNodes.get("room_275A_01")
    graph.addEdge(13,12,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299c_03")
    x2,y2 = dictOfNodes.get("room_210")
    graph.addEdge(40,41,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_210")
    x2,y2 = dictOfNodes.get("room_211")
    graph.addEdge(41,42,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_211")
    x2,y2 = dictOfNodes.get("room_212")
    graph.addEdge(42,43,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_212")
    x2,y2 = dictOfNodes.get("room_213")
    graph.addEdge(43,44,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_213")
    x2,y2 = dictOfNodes.get("room_214")
    graph.addEdge(44,45,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_214")
    x2,y2 = dictOfNodes.get("room_215")
    graph.addEdge(45,46,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_215")
    x2,y2 = dictOfNodes.get("room_216")
    graph.addEdge(46,47,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_263")
    x2,y2 = dictOfNodes.get("room_216")
    graph.addEdge(19,46,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_216")
    x2,y2 = dictOfNodes.get("room_217")
    graph.addEdge(47,48,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_217")
    x2,y2 = dictOfNodes.get("room_218")
    graph.addEdge(48,49,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_217")
    x2,y2 = dictOfNodes.get("room_264")
    graph.addEdge(48,15,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_218")
    x2,y2 = dictOfNodes.get("room_264")
    graph.addEdge(49,15,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_218")
    x2,y2 = dictOfNodes.get("room_219")
    graph.addEdge(49,50,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_219")
    x2,y2 = dictOfNodes.get("room_220")
    graph.addEdge(50,51,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_220")
    x2,y2 = dictOfNodes.get("room_221_01")
    graph.addEdge(51,52,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_264")
    x2,y2 = dictOfNodes.get("room_264_&_273")
    graph.addEdge(14,15,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_275A_02")
    x2,y2 = dictOfNodes.get("room_264_&_273")
    graph.addEdge(14,13,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_03")
    x2,y2 = dictOfNodes.get("room_272")
    graph.addEdge(5,25,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_272")
    x2,y2 = dictOfNodes.get("room_270_02")
    graph.addEdge(24,25,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_273")
    x2,y2 = dictOfNodes.get("room_270_02")
    graph.addEdge(24,16,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_273")
    x2,y2 = dictOfNodes.get("room_275A_02")
    graph.addEdge(16,13,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_273")
    x2,y2 = dictOfNodes.get("room_271A")
    graph.addEdge(16,17,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_271A")
    x2,y2 = dictOfNodes.get("room_271")
    graph.addEdge(17,18,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_271")
    x2,y2 = dictOfNodes.get("room_270_01")
    graph.addEdge(18,23,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_270_01")
    x2,y2 = dictOfNodes.get("road_299B_02")
    graph.addEdge(23,3,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_01")
    x2,y2 = dictOfNodes.get("road_299B_02")
    graph.addEdge(0,3,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_01")
    x2,y2 = dictOfNodes.get("room_207")
    graph.addEdge(0,22,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_01")
    x2,y2 = dictOfNodes.get("room_200")
    graph.addEdge(0,1,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_200")
    x2,y2 = dictOfNodes.get("room_206")
    graph.addEdge(1,2,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_01")
    x2,y2 = dictOfNodes.get("room_206")
    graph.addEdge(0,2,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_206")
    x2,y2 = dictOfNodes.get("road_209")
    graph.addEdge(2,4,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_299B_01")
    x2,y2 = dictOfNodes.get("road_209")
    graph.addEdge(0,4,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_200")
    x2,y2 = dictOfNodes.get("road_209")
    graph.addEdge(1,4,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_209")
    x2,y2 = dictOfNodes.get("room_221_02")
    graph.addEdge(4,53,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_206")
    x2,y2 = dictOfNodes.get("room_221_02")
    graph.addEdge(2,53,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_221_01")
    x2,y2 = dictOfNodes.get("room_221_02")
    graph.addEdge(52,53,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("terrace")
    x2,y2 = dictOfNodes.get("room_221_02")
    graph.addEdge(54,53,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("terrace")
    x2,y2 = dictOfNodes.get("room_206")
    graph.addEdge(2,54,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("terrace")
    x2,y2 = dictOfNodes.get("room_222_01")
    graph.addEdge(55,54,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_206")
    x2,y2 = dictOfNodes.get("room_222_01")
    graph.addEdge(55,2,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_222_01")
    x2,y2 = dictOfNodes.get("room_222_02")
    graph.addEdge(55,56,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_208")
    x2,y2 = dictOfNodes.get("room_222_01")
    graph.addEdge(55,93,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_200")
    x2,y2 = dictOfNodes.get("road_297A_12")
    graph.addEdge(1,111,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_206")
    x2,y2 = dictOfNodes.get("road_297A_12")
    graph.addEdge(2,111,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_206")
    x2,y2 = dictOfNodes.get("road_297A_08")
    graph.addEdge(2,90,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_08")
    x2,y2 = dictOfNodes.get("room_208")
    graph.addEdge(90,93,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_08")
    x2,y2 = dictOfNodes.get("room_205_03")
    graph.addEdge(90,92,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_12")
    x2,y2 = dictOfNodes.get("room_205_03")
    graph.addEdge(111,92,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_206")
    x2,y2 = dictOfNodes.get("room_205_03")
    graph.addEdge(2,92,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_206")
    x2,y2 = dictOfNodes.get("room_208")
    graph.addEdge(2,93,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_200")
    x2,y2 = dictOfNodes.get("road_297A_08")
    graph.addEdge(1,90,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_222_02")
    x2,y2 = dictOfNodes.get("room_223")
    graph.addEdge(56,57,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_223")
    x2,y2 = dictOfNodes.get("room_224")
    graph.addEdge(57,58,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_224")
    x2,y2 = dictOfNodes.get("room_225")
    graph.addEdge(58,59,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_225")
    x2,y2 = dictOfNodes.get("room_226")
    graph.addEdge(59,60,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_226")
    x2,y2 = dictOfNodes.get("room_227")
    graph.addEdge(60,61,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_227")
    x2,y2 = dictOfNodes.get("room_228")
    graph.addEdge(61,62,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_228")
    x2,y2 = dictOfNodes.get("room_229")
    graph.addEdge(62,63,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_229")
    x2,y2 = dictOfNodes.get("room_230")
    graph.addEdge(63,64,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_230")
    x2,y2 = dictOfNodes.get("room_231")
    graph.addEdge(64,65,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_231")
    x2,y2 = dictOfNodes.get("room_232")
    graph.addEdge(65,66,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_232")
    x2,y2 = dictOfNodes.get("room_233")
    graph.addEdge(66,67,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_233")
    x2,y2 = dictOfNodes.get("road_297B_01")
    graph.addEdge(67,68,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297B_01")
    x2,y2 = dictOfNodes.get("road_297B_02")
    graph.addEdge(68,69,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_259")
    x2,y2 = dictOfNodes.get("road_297B_02")
    graph.addEdge(69,70,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297B_02")
    x2,y2 = dictOfNodes.get("road_297B_03")
    graph.addEdge(69,71,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297B_03")
    x2,y2 = dictOfNodes.get("road_297A_01")
    graph.addEdge(71,72,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_01")
    x2,y2 = dictOfNodes.get("room_258")
    graph.addEdge(72,85,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_01")
    x2,y2 = dictOfNodes.get("road_297A_02")
    graph.addEdge(72,73,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_255")
    x2,y2 = dictOfNodes.get("road_297A_02")
    graph.addEdge(73,74,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_03")
    x2,y2 = dictOfNodes.get("road_297A_02")
    graph.addEdge(73,75,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_03")
    x2,y2 = dictOfNodes.get("room_254")
    graph.addEdge(75,82,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_254")
    x2,y2 = dictOfNodes.get("room_254_&_258")
    graph.addEdge(82,84,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_03")
    x2,y2 = dictOfNodes.get("road_297A_04")
    graph.addEdge(75,76,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_04")
    x2,y2 = dictOfNodes.get("road_250_01")
    graph.addEdge(76,77,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_04")
    x2,y2 = dictOfNodes.get("road_253_01")
    graph.addEdge(76,79,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_04")
    x2,y2 = dictOfNodes.get("road_297A_05")
    graph.addEdge(76,81,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_05")
    x2,y2 = dictOfNodes.get("road_297A_06")
    graph.addEdge(81,86,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_05")
    x2,y2 = dictOfNodes.get("room_254")
    graph.addEdge(81,82,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("room_254")
    x2,y2 = dictOfNodes.get("room_254_&_256")
    graph.addEdge(82,83,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_06")
    x2,y2 = dictOfNodes.get("road_205_01")
    graph.addEdge(86,87,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_06")
    x2,y2 = dictOfNodes.get("road_297A_07")
    graph.addEdge(86,89,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_07")
    x2,y2 = dictOfNodes.get("room_252")
    graph.addEdge(89,90,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_07")
    x2,y2 = dictOfNodes.get("road_297A_08")
    graph.addEdge(91,90,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297B_03")
    x2,y2 = dictOfNodes.get("road_297B_04")
    graph.addEdge(71,94,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297B_04")
    x2,y2 = dictOfNodes.get("room_257")
    graph.addEdge(94,95,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297B_04")
    x2,y2 = dictOfNodes.get("road_297B_05")
    graph.addEdge(94,96,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297B_05")
    x2,y2 = dictOfNodes.get("road_297")
    graph.addEdge(96,97,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297B_05")
    x2,y2 = dictOfNodes.get("road_297B_06")
    graph.addEdge(96,98,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297B_06")
    x2,y2 = dictOfNodes.get("road_249")
    graph.addEdge(98,113,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_249")
    x2,y2 = dictOfNodes.get("road_249A")
    graph.addEdge(113,114,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_249")
    x2,y2 = dictOfNodes.get("road_249C")
    graph.addEdge(113,116,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_249C")
    x2,y2 = dictOfNodes.get("road_249D")
    graph.addEdge(116,117,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_249C")
    x2,y2 = dictOfNodes.get("road_249B")
    graph.addEdge(115,116,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297B_06")
    x2,y2 = dictOfNodes.get("road_297A_01")
    graph.addEdge(98,72,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_01")
    x2,y2 = dictOfNodes.get("road_247")
    graph.addEdge(72,108,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_01")
    x2,y2 = dictOfNodes.get("road_297A_02")
    graph.addEdge(72,73,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_02")
    x2,y2 = dictOfNodes.get("road_245_02")
    graph.addEdge(73,107,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_02")
    x2,y2 = dictOfNodes.get("road_297A_03")
    graph.addEdge(73,75,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_245_01")
    x2,y2 = dictOfNodes.get("road_297A_03")
    graph.addEdge(75,106,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_03")
    x2,y2 = dictOfNodes.get("road_297A_04")
    graph.addEdge(75,76,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_04")
    x2,y2 = dictOfNodes.get("road_243_02")
    graph.addEdge(76,105,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_04")
    x2,y2 = dictOfNodes.get("road_297A_05")
    graph.addEdge(76,81,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_250_02")
    x2,y2 = dictOfNodes.get("road_297A_05")
    graph.addEdge(78,81,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_253_02")
    x2,y2 = dictOfNodes.get("road_297A_05")
    graph.addEdge(80,81,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_05")
    x2,y2 = dictOfNodes.get("road_297A_06")
    graph.addEdge(81,86,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_243_01")
    x2,y2 = dictOfNodes.get("road_297A_06")
    graph.addEdge(104,86,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_06")
    x2,y2 = dictOfNodes.get("road_297A_07")
    graph.addEdge(86,89,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_07")
    x2,y2 = dictOfNodes.get("road_205_02")
    graph.addEdge(88,89,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_07")
    x2,y2 = dictOfNodes.get("road_297A_08")
    graph.addEdge(89,91,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_08")
    x2,y2 = dictOfNodes.get("road_241_02")
    graph.addEdge(91,103,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_08")
    x2,y2 = dictOfNodes.get("road_297A_09")
    graph.addEdge(91,99,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_09")
    x2,y2 = dictOfNodes.get("road_297A_10")
    graph.addEdge(99,100,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_10")
    x2,y2 = dictOfNodes.get("road_297A_11")
    graph.addEdge(100,101,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_11")
    x2,y2 = dictOfNodes.get("road_297A_12")
    graph.addEdge(101,112,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_11")
    x2,y2 = dictOfNodes.get("road_241_01")
    graph.addEdge(101,102,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_11")
    x2,y2 = dictOfNodes.get("room_240")
    graph.addEdge(101,109,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_10")
    x2,y2 = dictOfNodes.get("room_240A")
    graph.addEdge(100,110,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_297A_09")
    x2,y2 = dictOfNodes.get("room_240B")
    graph.addEdge(99,111,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_205_02")
    x2,y2 = dictOfNodes.get("road_205_01")
    graph.addEdge(87,88,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_253_02")
    x2,y2 = dictOfNodes.get("road_253_01")
    graph.addEdge(79,80,calculateDistance(x1,y1,x2,y2))

    x1,y1 = dictOfNodes.get("road_250_02")
    x2,y2 = dictOfNodes.get("road_250_01")
    graph.addEdge(77,78,calculateDistance(x1,y1,x2,y2))

    return dictOfNodes,listOfKeys,graph



def reconstructPath(startVert, goalVert, preds):
    path = [goalVert]
    p = preds[goalVert]
    while p != None:
        path.insert(0, p)
        p = preds[p]
    return path

def heuristicDist(startVert, goalVert):
    dictOfNodes, listOfKeys, graph = dataInitialize()
    (x1,y1) = dictOfNodes.get(listOfKeys[int(startVert)])
    (x2,y2) = dictOfNodes.get(listOfKeys[int(goalVert)])
    return calculateDistance(x1,y1,x2,y2)



def AStarRoute(graph, startVert, goalVert):
    startVert = int(startVert)
    goalVert = int(goalVert)
    if startVert == goalVert:
        return []
    q = PriorityQueue()
    hCost = heuristicDist(startVert, goalVert)
    q.insert((startVert, None, 0), 0 + hCost)
    visited = set()
    pred = {}
    while not q.isEmpty():
        (fCost, data) = q.delete()
        (nextVert, previous, nextGCost) = fCost
        if nextVert not in visited:
            visited.add(nextVert)
            pred[nextVert] = previous
            print("--------------")
            print("Next vertex from queue:", nextVert, "  fCost =", fCost, "  g = ", nextGCost)
            if nextVert == goalVert:
                return reconstructPath(startVert, goalVert, pred)
            neighbors = graph.getNeighbors(int(nextVert))
            print("  Adding neighbors to to queue...")
            for n in neighbors:
                neighNode = n[0]
                edgeCost = n[1]
                if neighNode not in visited:
                    gCost = nextGCost + edgeCost
                    hCost = heuristicDist(startVert, goalVert)
                    print("    Node", neighNode, "From", nextVert)
                    print("    G cost =", gCost, 'H cost =', hCost, "F cost = ", gCost + hCost)
                    q.insert((neighNode, nextVert, gCost), gCost + hCost)
    print(visited)
    return [] # "NO PATH"



def pathFinder(self, startVert, goalVert):
    # startVert = input("Enter start vertice (in range between 0 and 155): ")
    # goalVert = input("Enter goal vertice (in range between 0 and 155): ")
    dictOfNodes, listOfKeys, graph = dataInitialize()
    route = AStarRoute(graph,startVert,goalVert)
    listOfRoute = []
    result = []
    for i in route:
        listOfRoute.append(listOfKeys[i])
        result.append(dictOfNodes.get(listOfKeys[i]))
    return listOfRoute, result
    

    
  