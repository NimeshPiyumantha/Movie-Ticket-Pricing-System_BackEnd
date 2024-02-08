from pydantic import BaseModel

class MoviesModel(BaseModel):
        mName: str;
        mYear: str;
        mCategory: str;
        mDuration: str;
        mLanguage: str;
        mDirector: str;