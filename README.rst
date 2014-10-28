=======
docomocvpy
=======

`docomo 画像認識 API`_ の Python ラッパーライブラリです。

.. image:: https://api.travis-ci.org/zaneli/docomocvpy.png?branch=master
   :target: https://travis-ci.org/zaneli/docomocvpy

Requirements
=======

- Python 3.4

Installation
=======

::

    $ pip install git+https://github.com/zaneli/docomocvpy

Usage
=======

::

    from docomocv import DocomoCVClient, Recog

    client = DocomoCVClient(<YOUR_API_KEY>)

    # Get image recognition candidates
    result = client.recognize('./food_package_img.jpg', Recog.food)

    # Send feedback
    client.feedback(result['recognitionId'], True)

    # Send feedback to each candidate
    client.feedback_to_candidate(result['recognitionId'], result['candidates'][0]['itemId'], True)


.. _`docomo 画像認識 API`: https://dev.smt.docomo.ne.jp/?p=docs.api.page&api_docs_id=102
