from post_office import mail


class SendEmail:

	def __init__(self):
		self.recipient = ''
		self.activation_token = ''

	@staticmethod
	def signup_welcome(recipient, VERIFICATION_URL=None, FIRST_NAME=None, LAST_NAME=None):

		mail.send(
				[recipient],
				template='signup_welcome',
				context={
					'VERIFICATION_URL': VERIFICATION_URL,
					'FIRST_NAME': FIRST_NAME,
					'LAST_NAME': LAST_NAME,
				},
				priority='now',
		)

	@staticmethod
	def password_reset(recipient, VERIFICATION_URL=None, FIRST_NAME=None, LAST_NAME=None):

		mail.send(
				[recipient],
				template='password_reset',
				context={
					'VERIFICATION_URL': VERIFICATION_URL,
					'FIRST_NAME': FIRST_NAME,
					'LAST_NAME': LAST_NAME,
				},
				priority='now',
		)
