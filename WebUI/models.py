from app import db

class so_code(db.Model):
    """"""
    __tablename__ = "code_result"

    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String)
    qid = db.Column(db.Integer)
    qurl=db.Column(db.String)
    qscore=db.Column(db.Float)
    
    def __init__(self, question, qid, qurl, qscore):
        """"""
        self.question = question 
        self.qid = qid
        self.qurl = qurl
        self.qscore = qscore


