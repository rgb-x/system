#!/bin/bash
 
echo "****************************************************************"
echo "* Delete gamepad hotkey buttons cfg retroarch - @yavimaya 2019 *"
echo "****************************************************************"

i=0; 

  for file in *.cfg;
    do
	echo $file
      cp $file $file.bak
	  sed -i "s/\(input_menu_toggle_btn *= *\).*/\1"\"nul"\"/" $file 
	  sed -i "s/\(input_exit_emulator_btn *= *\).*/\1"\"nul"\"/" $file 
	  sed -i "s/\(input_menu_toggle *= *\).*/\1"\"f1"\"/" $file 
	  sed -i "s/\(input_enable_hotkey_btn *= *\).*/\1"\"nul"\"/" $file 
	  sed -i "s/\(input_enable_hotkey_axis *= *\).*/\1"\"nul"\"/" $file 
	  sed -e 's/\(input_fps_toggle_btn *= *\).*/\1"nul"/' $file > tempfile.tmp
      mv tempfile.tmp $file
	  chmod +755 $file
	  rm $file.bak

    let i++;

      echo "Modified: " $file
    done

echo " *** All Done! *** Modified files:" $i