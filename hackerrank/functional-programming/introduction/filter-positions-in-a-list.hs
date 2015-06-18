f :: [Int] -> [Int]
f lst = map fst $ filter (odd.snd) indexed where
    indexed = zip lst [0..]

main = do
   inputdata <- getContents
   mapM_ (putStrLn. show). f. map read. lines $ inputdata
