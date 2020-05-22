import os
from pathlib import Path
#from platform import node
from e3smlab import E3SMlab
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

def test_verify(capsys):

    expdata = "/data/pace-exp-files/exp-acmetest-130.zip"
    #expdata = "/data/pace-exp-files"
    dbcfg = "%s/dbcfg.txt" % str(Path.home())

    assert os.path.isfile(dbcfg)

    with open(dbcfg) as f:
        myuser, mypwd, myhost, mydb = f.read().strip().split("\n")

    dburl = 'mysql+pymysql://%s:%s@%s/%s' % (myuser, mypwd, myhost, mydb)
    engine = create_engine(dburl)
    #Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    lab = E3SMlab()
    cmd = ["pacedb", expdata, "--db-session", "@session", "--verify"]
    ret, _ = lab.run_command(cmd, forward={"session": session})

    assert ret == 0

    captured = capsys.readouterr()
    assert (captured.out.strip() == "" or "failure" in captured.out)
    assert captured.err == ""
