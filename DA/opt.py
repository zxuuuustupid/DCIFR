import argparse

def parse_args():
    parser = argparse.ArgumentParser(description='DA Method')
 
    # basic parameters
    parser.add_argument('--model_name', type=str, default='IRM',
                        help='Name of the model (in ./models directory)')
    parser.add_argument('--source', type=str, default='source1kn',
                        help='Source data, separated by "," (select specific conditions of the dataset with name_number, such as CWRU_0)')
    parser.add_argument('--target', type=str, default='target1kn',
                        help='Target data (select specific conditions of the dataset with name_number, such as CWRU_0)')
    parser.add_argument('--data_dir', type=str, default="./datasets-leftaxlebox",
                        help='Directory of the datasets')
    parser.add_argument('--train_mode', type=str, default='single_source',
                        choices=['single_source', 'source_combine', 'multi_source'],
                        help='Training mode (select correctly before training)')
    parser.add_argument('--cuda_device', type=str, default='0',
                        help='Allocate the device to use only one GPU ('' means using cpu)')
    parser.add_argument('--max_epoch', type=int, default=2,
                        help='Number of epochs')
    parser.add_argument('--batch_size', type=int, default=1,
                        help='Batch size')
    parser.add_argument('--signal_size', type=int, default=0,
                        help='Signal length split by sliding window')
    parser.add_argument('--random_state', type=int, default=10,
                        help='Random state for the entire training')

    # optimizer parameters          
    parser.add_argument('--opt', type=str, choices=['sgd', 'adam'], default='sgd', help='Optimizer ')
    parser.add_argument('--momentum', type=float, default=0.9, help='Momentum for sgd')
    parser.add_argument('--betas', type=tuple, default=(0.9, 0.999), help='Betas for adam')
    parser.add_argument('--weight_decay', type=float, default=5e-4, help='Weight decay for both sgd and adam')
   
    # learning rate parameters
    parser.add_argument('--lr', type=float, default=0.001, help='Initial learning rate')
    parser.add_argument('--lr_scheduler', type=str, choices=['step', 'exp', 'stepLR', 'fix'], default='stepLR',
                        help='Type of learning rate schedule')
    parser.add_argument('--gamma', type=float, default=0.2,
                        help='Parameter for the learning rate scheduler (except "fix")')
    parser.add_argument('--steps', type=str, default='10',
                        help='Step of learning rate decay for "step" and "stepLR"')
    
    # optimization parameters
    parser.add_argument('--backbone', type=str, default='CNN', choices=['CNN', 'ResNet'],
                        help='The backbone used to construct the training model (defined in ./modules)')
    parser.add_argument('--num_workers', type=int, default=0,
                        help='Number of workers for dataloader')
    parser.add_argument('--normlize_type', type=str, choices=['0-1', '-1-1', 'mean-std'], default='-1-1',
                        help='Data normalization methods')
    parser.add_argument('--tradeoff', type=list, default=['exp', 'exp', 'exp'],
                        help='Trade-off coefficients for the sum of loss terms. Use integer or "exp" ("exp" represents an increase from 0 to 1 during training)')
    parser.add_argument('--zeta', type=float, default=10.0,
                        help='Parameter to control the increasing rate of "exp" tradeoff')
    parser.add_argument('--dropout', type=float, default=0., help='Dropout layer coefficient')
    
    # save and load
    parser.add_argument('--save', type=bool, default=True, help='Save logs and trained model checkpoints')
    parser.add_argument('--save_dir', type=str, default='./ckpt',
                        help='Directory to save logs and model checkpoints')
    parser.add_argument('--load_path', type=str, default='',
                        help='Load trained model checkpoints from this path (for testing, not for resuming training)')
    args = parser.parse_args()
    return args
    
