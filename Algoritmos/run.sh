python makeDats.py
mv *.dat dats/

cd ResultadosGLPK

glpsol -m ../mdgp.mod -d ../dats/Geo_n010_ss_10.dat -o Geo_n010_ss_10.sol --tmlim 3600 | tee Geo_n010_ss_10.txt
glpsol -m ../mdgp.mod -d ../dats/RanInt_n010_ds_07.dat -o RanInt_n010_ds_07.sol --tmlim 3600 | tee RanInt_n010_ds_07.txt
glpsol -m ../mdgp.mod -d ../dats/RanInt_n010_ss_10.dat -o RanInt_n010_ss_10.sol --tmlim 3600 | tee RanInt_n010_ss_10.txt
glpsol -m ../mdgp.mod -d ../dats/RanReal_n010_ss_10.dat -o RanReal_n010_ss_10.sol --tmlim 3600 | tee RanReal_n010_ss_10.txt
glpsol -m ../mdgp.mod -d ../dats/RanInt_n012_ss_03.dat -o RanInt_n012_ss_03.sol --tmlim 3600 | tee RanInt_n012_ss_03.txt
glpsol -m ../mdgp.mod -d ../dats/Geo_n030_ds_08.dat -o Geo_n030_ds_08.sol --tmlim 3600 | tee Geo_n030_ds_08.txt
glpsol -m ../mdgp.mod -d ../dats/RanInt_n030_ss_05.dat -o RanInt_n030_ss_05.sol --tmlim 3600 | tee RanInt_n030_ss_05.txt
glpsol -m ../mdgp.mod -d ../dats/Geo_n060_ss_04.dat -o Geo_n060_ss_04.sol --tmlim 3600 | tee Geo_n060_ss_04.txt
glpsol -m ../mdgp.mod -d ../dats/RanInt_n060_ds_03.dat -o RanInt_n060_ds_03.sol --tmlim 3600 | tee RanInt_n060_ds_03.txt
glpsol -m ../mdgp.mod -d ../dats/RanReal_n060_ss_04.dat -o RanReal_n060_ss_04.sol --tmlim 3600 | tee RanReal_n060_ss_04.txt