# from marllib import marl
# ia2c = marl.algos.ia2c(hyperparam_source='common')
# env = marl.make_env(environment_name="mpe", map_name="simple_spread") #pettingzoo_env 초기화
# model = marl.build_model(env, ia2c, {"core_arch": "mlp_p", "encode_layer": "64-64"}) #"128-256"
# ia2c.fit(env, model, stop={"timesteps_total": 1000000}, checkpoint_freq=100, share_policy="group")

from marllib import marl
qmix = marl.algos.qmix(hyperparam_source='common')
env = marl.make_env(environment_name="mpe", map_name="simple_spread") #pettingzoo_env 초기화
model = marl.build_model(env, qmix, {"core_arch": "mlp", "encode_layer": "64-64"}) #"128-256"
qmix.fit(env, model, stop={"timesteps_total": 1000000}, checkpoint_freq=100, share_policy="group")