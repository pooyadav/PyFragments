(*In the /owl/examples:
wget http://yann.lecun.com/exdb/mnist/train-images-idx3-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/train-labels-idx1-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/t10k-images-idx3-ubyte.gz
wget http://yann.lecun.com/exdb/mnist/t10k-labels-idx1-ubyte.gz
gzip -d *.gz
*)
open Core.Std;;

let read_int32_be in_channel =
  let b1 = Option.value_exn (In_channel.input_byte in_channel) in
  let b2 = Option.value_exn (In_channel.input_byte in_channel) in
  let b3 = Option.value_exn (In_channel.input_byte in_channel) in
  let b4 = Option.value_exn (In_channel.input_byte in_channel) in
  b4 + 256 * (b3 + 256 * (b2 + 256 * b1))

let read_images filename =
  let in_channel = In_channel.create filename in
  let magic_number = read_int32_be in_channel in
  (* if magic_number <> 2051
  then Printf.failwithf "Incorrect magic number in %s: %d" filename magic_number (); *)
  let samples = read_int32_be in_channel in
  let rows = read_int32_be in_channel in
  let columns = read_int32_be in_channel in
  let data =
    Bigarray.Array2.create Bigarray.float32 Bigarray.c_layout samples (rows * columns)
  in
  for sample = 0 to samples - 1 do
    for idx = 0 to rows * columns - 1 do
      let v = Option.value_exn (In_channel.input_byte in_channel) in
      Bigarray.Array2.set data sample idx (Float.of_int v);
    done;
  done; 
  In_channel.close in_channel;
  data

let read_labels filename =
  let in_channel = In_channel.create filename in
  let magic_number = read_int32_be in_channel in
  let col = 10 in
  if magic_number <> 2049
  then Printf.failwithf "Incorrect magic number in %s: %d" filename magic_number ();
  let samples = read_int32_be in_channel in
  let data = Bigarray.Array2.create Bigarray.float32 Bigarray.c_layout samples col in
  for sample = 0 to samples - 1 do
    let v = Option.value_exn (In_channel.input_byte in_channel) in
    Bigarray.Array2.set data sample v (Float.of_int 1);
  done;
  In_channel.close in_channel;
  data;;

let test_imagename = "./examples/t10k-images-idx3-ubyte" 
let train_imagename = "./examples/train-images-idx3-ubyte"
let test_labelname = "./examples/t10k-labels-idx1-ubyte"
let train_labelname = "./examples/train-labels-idx1-ubyte"

let test_image = read_images test_imagename
let train_image = read_images train_imagename
let test_label = read_labels test_labelname
let train_label = read_labels train_labelname

let x = train_image;;
let y = train_label;;

(*====*)

#require "owl_neural";;
open Owl_neural;;

(* config the neural network *)
let nn = Feedforward.create ();;
let l0 = linear ~inputs:784 ~outputs:300 ~init_typ:Init.(Uniform (-0.075,0.075));;
let l1 = linear ~inputs:300 ~outputs:10 ~init_typ:Init.(Uniform (-0.075,0.075));;
Feedforward.add_layer nn l0;;
Feedforward.add_activation nn Activation.Tanh;;
Feedforward.add_layer nn l1;;
Feedforward.add_activation nn Activation.Softmax;;
print nn;;

let x, _, y = Dataset.load_mnist_train_data ();;
let x, y = Algodiff.AD.Mat x, Algodiff.AD.Mat y;;

(* plot loss history *)
let l = train nn x y;;
let p = Vec.sequential (Array.length l);;
let q = Vec.of_array l;;
Plot.plot p q;;

(* test the nn model *)
let x, y, _ = Dataset.load_mnist_test_data () in
let x, y = Dataset.draw_samples x y 10 in
test_model nn (Mat x) (Mat y);;




(* Dataset.print_mnist_image (Dense.Matrix.S.row data 0);;*)

(* let read_images filename =
  let in_channel = In_channel.create filename in
  let magic_number = read_int32_be in_channel in
  if magic_number <> 2051
  then Printf.failwithf "Incorrect magic number in %s: %d" filename magic_number (); 
  let samples = read_int32_be in_channel in
  let rows = read_int32_be in_channel in
  let columns = read_int32_be in_channel in
  let data =
    Bigarray.Array2.create Bigarray.float32 Bigarray.c_layout samples (rows * columns)
  in
  for sample = 0 to samples - 1 do
    for idx = 0 to rows * columns - 1 do
      let v = Option.value_exn (In_channel.input_byte in_channel) in
      Bigarray.Array2.set data sample idx Float.(of_int v / 255.);
    done;
  done; 
  In_channel.close in_channel;
  data *)