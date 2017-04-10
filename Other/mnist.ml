#require "owl_neural";;
open Owl_neural;;

(* config the neural network *)
let nn = Feedforward.create ();;
(* let l0 = linear ~inputs:784 ~outputs:300 ~init_typ:Init.(Uniform (-0.075,0.075));;
let l1 = linear ~inputs:300 ~outputs:10 ~init_typ:Init.(Uniform (-0.075,0.075));; *)
let l0 = linear ~inputs:784 ~outputs:300 ~init_typ:Init.(Gaussian (0., 0.075));;
let l1 = linear ~inputs:300 ~outputs:10 ~init_typ:Init.(Gaussian (0., 0.075));;
Feedforward.add_layer nn l0;;
Feedforward.add_activation nn Activation.Tanh;;
Feedforward.add_layer nn l1;;
Feedforward.add_activation nn Activation.Softmax;;
print nn;;

(* load data and config training *)
(*  let x, _, y = Dataset.load_mnist_train_data ();; *)
let x, y = Algodiff.AD.Mat x, Algodiff.AD.Mat y;;
let params = Owl_neural_optimise.Params.default ();;
params.learning_rate <- Owl_neural_optimise.Learning_Rate.Const 0.1;;
(* params.learning_rate <- Owl_neural_optimise.Learning_Rate.Adagrad 0.01;; *)
(* params.learning_rate <- Owl_neural_optimise.Learning_Rate.RMSprop (0.001, 0.9);; *)
(* params.momentum <- Owl_neural_optimise.Momentum.Nesterov 0.9;; *)
let l = train ~params nn x y;;

(* plot loss history *)
let p = Vec.sequential (Array.length l);;
let q = Vec.of_array l;;
Plot.plot p q;;

(* test the nn model *)
let x, y, _ = Dataset.load_mnist_test_data () in
let x, y = Dataset.draw_samples x y 10 in
test_model nn (Mat x) (Mat y);;