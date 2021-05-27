(defun fn (n)
    (loop repeat n
        do (format t "Hello World~%")))
(fn (read))
