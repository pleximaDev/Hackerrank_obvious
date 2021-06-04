{-# LANGUAGE DuplicateRecordFields, FlexibleInstances, UndecidableInstances #-}

module Main where

import Control.Monad
import Data.Array
import Data.Bits
import Data.List
import Data.List.Split
import Data.Set
import Data.Text
import Debug.Trace
import System.Environment
import System.IO
import System.IO.Unsafe

rotLeft a d = do -- INTEGER_ARRAY a; INTEGER d;--return INTEGER_ARRAY--
    let len = Data.List.length a
    let shift = abs(len - (mod d len))
    Data.List.drop (len - shift) a ++ Data.List.take (len - shift) a

lstrip = Data.Text.unpack . Data.Text.stripStart . Data.Text.pack
rstrip = Data.Text.unpack . Data.Text.stripEnd . Data.Text.pack

main :: IO()
main = do
    stdout <- getEnv "OUTPUT_PATH"
    fptr <- openFile stdout WriteMode

    firstMultipleInputTemp <- getLine
    let firstMultipleInput = Data.List.words $ rstrip firstMultipleInputTemp

    let n = read (firstMultipleInput !! 0) :: Int

    let d = read (firstMultipleInput !! 1) :: Int

    aTemp <- getLine

    let a = Data.List.map (read :: String -> Int) . Data.List.words $ rstrip aTemp

    let result = rotLeft a d

    hPutStrLn fptr $ Data.List.intercalate " " $ Data.List.map (\x -> show x) $ result

    hFlush fptr
    hClose fptr
