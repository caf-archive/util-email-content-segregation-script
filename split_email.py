#
# Copyright 2015-2017 Hewlett Packard Enterprise Development LP.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# coding=UTF-8
import talon
from talon import quotations
from talon import signature
from talon.signature.bruteforce import extract_signature

# don't forget to init the library first
# it loads machine learning classifiers
talon.init()


def splitEmail(message):
    return quotations.split_emails(message)



def extractSignature(message):
	body, signature = extract_signature(message)
	return body, signature


def extractSignature_MachineLearning(message, sender):
	body, sig = signature.extract(message, sender=sender)
	return body, sig