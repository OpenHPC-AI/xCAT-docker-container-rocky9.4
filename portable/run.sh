#!/bin/bash

docker run -itd   --name xcat   --hostname cn08  --network host   --restart unless-stopped    -v /sys/fs/cgroup:/sys/fs/cgroup:ro   -v /xcat_pv/xcatdata:/xcatdata   -v /xcat_pv/var_log_xcat:/var/log/xcat   -v /xcat_pv/xcat_mysqldata:/var/lib/mysql   -v /xcat_pv/xcatcont_sshkey/.ssh:/root/.ssh --env-file .env xcat_rocky9.4:2.17.0
