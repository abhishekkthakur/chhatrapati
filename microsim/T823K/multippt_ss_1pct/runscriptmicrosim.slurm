#!/bin/bash
 
#SBATCH --job-name=T_823K_ss_1pct_multippt
###SBATCH --account=at809449
#SBATCH --mail-user=809449@tatasteel.com
#SBATCH --partition=cpu
#SBATCH --ntasks=160
#SBATCH --ntasks-per-node=40
#SBATCH --nodes=4
#SBATCH --mem=128gb
#SBATCH --time=120:00:00
#SBATCH --output=results_%A.out
#SBATCH --error=results_%A.err
#export PSM2_MULTI_EP=0
cd $SLURM_SUBMIT_DIR
export FI_TCP_IFACE=ib0
export FI_PROVIDER=PSM2
export I_MPI_FABRICS=shm:ofi
export I_MPI_FALLBACK=0
ulimit -l unlimited
ulimit -s unlimited
date
srun --mpi=pmi2 --kill-on-bad-exit=1 -n 160 /rnd_hpc_data/apps/MicroSim-4.0/Grand_potential_Finite_difference_2D_MPI/microsim_gp Input_FNF_1.in Fill.in output 16 10
/rnd_hpc_data/apps/MicroSim-4.0/Grand_potential_Finite_difference_2D_MPI/write_xdmf Input_FNF_1.in output 0 10000000
date
