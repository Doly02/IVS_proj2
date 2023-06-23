#######################################################
 # Název projektu: Kalkulačka
 # Soubor: CMakeLists.txt
 # Datum: 13.4.2023
 # Poslední změna: 17.4.2023
 # Autor: Tomas Dolak 
 # Tým: Tomojavo
 # 
 # Popis: Kod slouzi pro vytvoreni instalatoru aplikace kalkulacky TOMOJAVO_CALC 
#######################################################
##
# @file CMakeList.txt
# @author Tomas Dolak
#
# @brief Kod slouzi pro vytvoreni instalatoru aplikace kalkulacky TOMOJAVO_CALC
##

cmake_minimum_required(VERSION 3.0)


project(TOMOJAVO_CALC VERSION 1.0)

# kontrola zda je python a knihovna tkinter pritomna v PC
find_package(Python3 COMPONENTS Interpreter Development)
if(NOT Python3_FOUND)
    message(STATUS "Python3 not found, trying to install...\n")
    execute_process(
        COMMAND sudo apt-get install -y python3
        RESULT_VARIABLE _python_install_result
    )
    if(NOT _python_install_result EQUAL 0)
        message(FATAL_ERROR "Failed to install Python3, please install it manually.\n")
    else()
        find_package(Python3 COMPONENTS Interpreter Development) # Znovu zkontrolujte Python3 po instalaci
    endif()
endif()
# kontrola zda je nalezena i knihovna tkinter
if(Python3_FOUND)
    execute_process(
        COMMAND
        "${Python3_EXECUTABLE}" -c "import tkinter"
        RESULT_VARIABLE _tkinter_check_result
        OUTPUT_QUIET
        ERROR_QUIET
    )
    if(NOT _tkinter_check_result EQUAL 0) # jestlize nebyla nalezena knihovna tkinter 
        message(STATUS "Python tkinter library not found, trying to install...\n")
        execute_process(
            COMMAND sudo apt-get install python3-tk
            RESULT_VARIABLE _tkinter_install_result
        )
        if(NOT _tkinter_install_result EQUAL 0)
            message(FATAL_ERROR "Failed to install Python tkinter library, please install it manually.\n")
        endif()
    endif()
endif()




# cile z makefilu pro CMake
add_custom_target(build COMMAND make build)
add_custom_target(pack COMMAND make pack)
add_custom_target(make_clean COMMAND make clean) # Změna názvu cíle z "clean" na "make_clean"
add_custom_target(test COMMAND make test)
add_custom_target(doc COMMAND make doc)
add_custom_target(run COMMAND make run)
add_custom_target(profile COMMAND make profile)

    
#nastaveni 
file(GLOB PYTHON_SCRIPTS src/*.py)
install(PROGRAMS ${PYTHON_SCRIPTS} DESTINATION /usr/local/bin/tomojavo_calc/src)
install(PROGRAMS src/main.py DESTINATION /usr/local/bin/tomojavo_calc/src RENAME "TOMOJAVO_CALC")


install(DIRECTORY ${CMAKE_SOURCE_DIR}/assets DESTINATION /usr/local/bin/tomojavo_calc)


# vytvori skript, ktery umozni spusteni kalkulacky po prikazu TOMOJAVO_CALC
file(WRITE ${CMAKE_CURRENT_BINARY_DIR}/tomojavo_calc_launcher
"#!/bin/sh\n\
exec python3 /usr/local/bin/tomojavo_calc/src/TOMOJAVO_CALC \"\$@\"\n")
install(PROGRAMS ${CMAKE_CURRENT_BINARY_DIR}/tomojavo_calc_launcher DESTINATION /usr/local/bin RENAME TOMOJAVO_CALC)


# Instalace ikony
install(FILES ${CMAKE_SOURCE_DIR}/assets/Tomojavo_icon.png DESTINATION /usr/share/icons/hicolor/48x48/apps RENAME Tomojavo_icon.png)

# Instalace .desktop file
configure_file(TomojavoCalc.desktop.in TomojavoCalc.desktop)
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/TomojavoCalc.desktop DESTINATION /usr/share/applications)


#nastaveni Cpack
set(CPACK_GENERATOR "DEB")
set(CPACK_DEBIAN_PACKAGE_DEPENDS "python3, python3-tk")
set(CPACK_PACKAGE_FILE_NAME "${CMAKE_PROJECT_NAME}-${PROJECT_VERSION}-${CMAKE_SYSTEM_NAME}")


set(CPACK_PACKAGE_NAME "TomojavoCalc")

set(CPACK_PACKAGE_VENDOR "VUT FIT")
set(CPACK_DEBIAN_PACKAGE_MAINTAINER "Tomas Dolak <xdolak09@fit.vutbr.cz>")
set(CPACK_PACKAGE_DESCRIPTION_SUMMARY "TomojavoCalc - LICENCE GNU 3.0 ")
set(CPACK_PACKAGE_VERSION "${PROJECT_VERSION}")
set(CPACK_PACKAGE_INSTALL_DIRECTORY "TomojavoCalc")

include(CPack)