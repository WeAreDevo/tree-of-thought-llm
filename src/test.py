import argparse
from tot.methods.bfs_watsonx import solve
from tot.tasks.qa4pc import QA4PC

args = argparse.Namespace(
    backend="meta-llama/llama-2-70b-chat",
    temperature=0.7,
    task="qa4pc",
    naive_run=False,
    prompt_sample="cot",
    method_generate="sample",
    method_evaluate="vote",
    method_select="greedy",
    n_generate_sample=3,
    n_evaluate_sample=3,
    n_select_sample=2,
)

task = QA4PC()
ys, infos = solve(args, task, 0)
print(ys[0])
